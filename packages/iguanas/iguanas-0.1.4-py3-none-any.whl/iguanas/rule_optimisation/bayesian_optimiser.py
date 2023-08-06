"""Optimises a set of rules using Bayesian Optimisation."""
import iguanas.utils as utils
from iguanas.utils.types import NumpyArray, PandasDataFrame, PandasSeries
from iguanas.utils.typing import PandasDataFrameType, PandasSeriesType
from iguanas.rule_optimisation._base_optimiser import _BaseOptimiser
import pandas as pd
from typing import Callable, Dict, List, Set, Tuple
from hyperopt import hp, tpe, fmin
from hyperopt.pyll import scope
import numpy as np
from joblib import Parallel, delayed


class BayesianOptimiser(_BaseOptimiser):
    """
    Optimises a set of rules (given in the standard Iguanas lambda expression
    format) using Bayesian Optimisation.

    Parameters
    ----------
    rule_lambdas : Dict[str, Callable[[Dict], str]]
        Set of rules defined using the standard Iguanas lambda expression
        format (values) and their names (keys).
    lambda_kwargs : Dict[str, Dict[str, float]]
        For each rule (keys), a dictionary containing the features used in the
        rule (keys) and the current values (values).
    metric : Callable
        The optimisation function used to calculate the metric which the rules
        are optimised for (e.g. F1 score).
    n_iter : int
        The number of iterations that the optimiser should perform.
    algorithm : Callable, optional
        The algorithm leveraged by hyperopt's `fmin` function, which
        optimises the rules. Defaults to tpe.suggest, which corresponds to
        Tree-of-Parzen-Estimator.
    num_cores : int, optional
        The number of cores to use when optimising the rule thresholds.
        Defaults to 1.
    verbose : int, optional
        Controls the verbosity - the higher, the more messages. >0 : shows
        the overall progress of the optimisation process; >1 : shows the
        progress of the optimisation of each rule, as well as the overall
        optimisation process. Note that setting `verbose` > 1 only works
        when `num_cores` = 1. Defaults to 0.
    **kwargs : tuple , optional
        Any additional keyword arguments to pass to hyperopt's `fmin`
        function.

    Attributes
    ----------
    rule_strings : Dict[str, str]
        The optimised + unoptimisable (but applicable) rules, defined using the
        standard Iguanas string format (values) and their names (keys).
    rule_lambdas : Dict[str, object]
        The optimised rules + unoptimisable (but applicable), defined using the
        standard Iguanas lambda expression format (values) and their names
        (keys).
    lambda_kwargs : Dict[str, object]
        The keyword arguments for the optimised + unoptimisable (but
        applicable) rules defined using the standard Iguanas lambda expression
        format.
    rules : Rules
        The Rules object containing the optimised + unoptimisable (but
        applicable) rules.
    rule_names : List[str]
        The names of the optimised + unoptimisable (but applicable) rules.
    rule_names_missing_features : List[str]
        Names of rules which use features that are not present in the dataset
        (and therefore can't be optimised or applied).
    rule_names_no_opt_conditions : List[str]
        Names of rules which have no optimisable conditions (e.g. rules that
        only contain string-based conditions).
    rule_names_zero_var_features : List[str]
        Names of rules which exclusively contain zero variance features (based
        on `X`), so cannot be optimised.
    opt_rule_performances : Dict[str, float]
        The optimisation metric (values) calculated for each optimised rule
        (keys).
    orig_rule_performances : Dict[str, float]
        The optimisation metric (values) calculated for each original rule
        (keys).
    non_optimisable_rules : Rules
        A `Rules` object containing the rules which contained exclusively
        non-optimisable conditions.
    zero_varaince_rules : Rules
        A `Rules` object containing the rules which contained exclusively zero
        variance features.

    Examples
    --------
    >>> from iguanas.rule_optimisation import BayesianOptimiser
    >>> from iguanas.rules import Rules
    >>> from iguanas.metrics import FScore
    >>> import pandas as pd
    >>> X = pd.DataFrame({
    ...     'A': [0.9, 0.2, 0.1, 0.3],
    ...     'B': [0.01, 0.2, 0.5, 0.1]
    ... })
    >>> y = pd.Series([
    ...     1, 0, 1, 0
    ... ])
    >>> f1 = FScore(beta=1)
    >>> rule_strings = {
    ...     'Rule1': "X['A']>0",
    ...     'Rule2': "X['B']>1",
    ...     'Rule3': "(X['A']>0)|(X['B']>0)"
    ... }
    >>> rules = Rules(rule_strings=rule_strings)
    >>> rule_lambdas = rules.as_rule_lambdas(
    ...     as_numpy=False, 
    ...     with_kwargs=True
    ... )
    >>> bo = BayesianOptimiser(
    ...     rule_lambdas=rule_lambdas, 
    ...     lambda_kwargs=rules.lambda_kwargs, 
    ...     metric=f1.fit, 
    ...     n_iter=10
    ... )
    >>> X_rules = bo.fit(X=X, y=y)
    >>> print(X_rules)
       Rule1  Rule2  Rule3
    0      1      0      1
    1      1      0      0
    2      1      1      1
    3      1      0      0
    >>> print(bo.rule_strings)
    {'Rule1': "(X['A']>0)", 'Rule2': "(X['B']>0.2481631882805597)", 'Rule3': "(X['A']>0.648569854008818)|(X['B']>0.2481631882805597)"}
    >>> print(bo.opt_rule_performances)
    {'Rule1': 0.6666666666666666, 'Rule2': 0.6666666666666666, 'Rule3': 1.0}
    >>> X_rules = bo.transform(X=X)
    >>> print(X_rules)
       Rule1  Rule2  Rule3
    0      1      0      1
    1      1      0      0
    2      1      1      1
    3      1      0      0
    """

    def __init__(self,
                 rule_lambdas: Dict[str, Callable],
                 lambda_kwargs: Dict[str, Dict[str, float]],
                 metric: Callable,
                 n_iter: int,
                 algorithm=tpe.suggest,
                 num_cores=1,
                 verbose=0,
                 **kwargs):
        _BaseOptimiser.__init__(
            self, rule_lambdas=rule_lambdas, lambda_kwargs=lambda_kwargs,
            metric=metric, num_cores=num_cores, verbose=verbose
        )
        self.n_iter = n_iter
        self.algorithm = algorithm
        self.kwargs = kwargs
        self.rule_strings = {}
        self.rule_names = []

    def __repr__(self):
        if self.rule_strings == {}:
            return f'BayesianOptimiser object with {len(self.orig_rule_lambdas)} rules to optimise'
        else:
            return f'BayesianOptimiser object with {len(self.optimisable_rules.rule_strings)} optimised rules and {len(self.non_optimisable_rules.rule_strings)} unoptimisable rules'

    def fit(self,
            X: PandasDataFrameType,
            y=None,
            sample_weight=None) -> PandasDataFrameType:
        """
        Optimises a set of rules (given in the standard Iguanas lambda expression
        format) using Bayesian Optimisation.

        Parameters
        ----------
        X : PandasDataFrameType
            The feature set.
        y : PandasSeriesType, optional
            The binary target column. Not required if optimising rules on
            unlabelled data. Defaults to None.
        sample_weight : PandasSeriesType, optional
            Record-wise weights to apply. Defaults to None.

        Returns
        -------
        PandasDataFrameType
            The binary columns of the optimised + unoptimisable (but
            applicable) rules on the fitted dataset.
        """

        X_min, X_max, orig_X_rules = self._prepare_rules_for_opt(
            X=X,
            y=y,
            sample_weight=sample_weight
        )
        # Generate dictionary of space functions (for optimisation)
        int_cols = self._return_int_cols(X=X)
        rule_features_set_tagged = set().union(
            *[list(lambda_kwarg.keys()) for lambda_kwarg in self.orig_rules.lambda_kwargs.values()]
        )
        all_space_funcs = self._return_all_space_funcs(
            rule_features_set_tagged=rule_features_set_tagged,
            X_min=X_min,
            X_max=X_max,
            int_cols=int_cols
        )
        # Optimise rules
        opt_rule_strings = self._optimise_rules(
            rule_lambdas=self.optimisable_rules.rule_lambdas,
            lambda_kwargs=self.optimisable_rules.lambda_kwargs,
            X=X,
            y=y,
            sample_weight=sample_weight,
            int_cols=int_cols,
            all_space_funcs=all_space_funcs
        )
        X_rules = self._return_final_rule_set(
            X=X,
            y=y,
            sample_weight=sample_weight,
            opt_rule_strings=opt_rule_strings,
            orig_X_rules=orig_X_rules
        )
        return X_rules

    def _optimise_rules(self,
                        rule_lambdas: Dict[str, Callable[[Dict], str]],
                        lambda_kwargs: Dict[str, Dict[str, float]],
                        X: PandasDataFrameType,
                        y: PandasSeriesType,
                        sample_weight: PandasSeriesType,
                        int_cols: list,
                        all_space_funcs: dict) -> Dict[str, str]:
        """Optimises each rule in the set"""

        opt_rule_strings = {}
        rule_lambdas_items = utils.return_progress_ready_range(
            verbose=self.verbose, range=rule_lambdas.items()
        )
        with Parallel(n_jobs=self.num_cores) as parallel:
            opt_rule_strings_list = parallel(delayed(self._optimise_single_rule)(
                rule_name, rule_lambda, lambda_kwargs, X, y, sample_weight,
                int_cols, all_space_funcs
            ) for rule_name, rule_lambda in rule_lambdas_items
            )
        opt_rule_strings = dict(opt_rule_strings_list)
        return opt_rule_strings

    def _optimise_single_rule(self,
                              rule_name: str,
                              rule_lambda: object,
                              lambda_kwargs: Dict[str, Dict[str, float]],
                              X: PandasDataFrameType,
                              y: PandasSeriesType,
                              sample_weight: PandasSeriesType,
                              int_cols: List[str],
                              all_space_funcs: dict) -> Tuple[str, str]:
        """Optimises a single rule"""

        if self.verbose > 1:
            print(f'Optimising rule `{rule_name}`')
        rule_lambda_kwargs = lambda_kwargs[rule_name]
        rule_features = list(rule_lambda_kwargs.keys())
        rule_space_funcs = self._return_rule_space_funcs(
            all_space_funcs=all_space_funcs, rule_features=rule_features)
        opt_thresholds = self._optimise_rule_thresholds(
            rule_lambda=rule_lambda, rule_space_funcs=rule_space_funcs, X_=X,
            y=y, sample_weight=sample_weight, metric=self.metric, n_iter=self.n_iter,
            algorithm=self.algorithm, verbose=self.verbose, kwargs=self.kwargs)
        opt_thresholds = self._convert_opt_int_values(
            opt_thresholds=opt_thresholds, int_cols=int_cols)
        return rule_name, rule_lambda(**opt_thresholds)

    @staticmethod
    def _return_int_cols(X: PandasDataFrameType) -> List[str]:
        """Returns the list of integer columns"""

        int_cols = X.select_dtypes(include=np.int).columns.tolist()
        float_cols = X.select_dtypes(include=np.float).columns.tolist()
        for float_col in float_cols:
            if abs(X[float_col] - X[float_col].round()).sum() == 0:
                int_cols.append(float_col)
        return int_cols

    @staticmethod
    def _return_all_space_funcs(rule_features_set_tagged: Set[str],
                                X_min: PandasSeriesType,
                                X_max: PandasSeriesType,
                                int_cols: List[str]) -> Dict[str, hp.uniform]:
        """
        Returns a dictionary of the space function (used in the optimiser) for 
        each feature in the dataset
        """
        space_funcs = {}
        for feature in rule_features_set_tagged:
            # If features contains %, means that there's more than one
            # occurance of the feature in the rule. To get the column, we need
            # to get the string precending the % symbol.
            col = feature.split('%')[0]
            col_min = X_min[col]
            col_max = X_max[col]
            # If column is zero variance (and all np.nan), then set the space
            # function to 0
            if np.isnan(col_min) and np.isnan(col_max):
                space_func = 0
            # If column is zero variance (excl. nulls), then set the space
            # function to the minimum value
            elif col_min == col_max:
                space_func = col_min
            elif col in int_cols:
                space_func = scope.int(
                    hp.uniform(feature, col_min, col_max)
                )
            else:
                space_func = hp.uniform(feature, col_min, col_max)
            space_funcs[feature] = space_func
        return space_funcs

    @staticmethod
    def _return_rule_space_funcs(all_space_funcs: Dict[str, hp.uniform],
                                 rule_features: List[str]) -> Dict[str, hp.uniform]:
        """
        Returns a dictionary of the space function for each feature in 
        the rule.
        """
        rule_space_funcs = dict(
            (rule_feature, all_space_funcs[rule_feature])
            for rule_feature in rule_features
        )
        return rule_space_funcs

    @staticmethod
    def _optimise_rule_thresholds(rule_lambda: Callable[[Dict], str],
                                  rule_space_funcs: Dict[str, hp.uniform],
                                  X_: PandasDataFrameType,
                                  y: PandasSeriesType,
                                  sample_weight: PandasSeriesType,
                                  metric: Callable,
                                  algorithm: Callable,
                                  n_iter: int,
                                  verbose: int,
                                  kwargs: dict) -> Dict[str, float]:
        """Calculates the optimal rule thresholds"""

        def _objective(rule_space_funcs: Dict[str, hp.uniform]) -> float:
            """
            Evaluates the optimisation metric for each
            iteration in the optimisation process.
            """
            # Bring X_ into local scope (for eval() function)
            X = X_
            rule_string = rule_lambda(**rule_space_funcs)
            y_pred = eval(rule_string)
            # If evaluated rule is PandasSeriesType, replace pd.NA with False
            # (since pd.NA used in any condition returns pd.NA, not False as with
            # numpy)
            if utils.is_type(y_pred, [PandasSeries]):
                y_pred = y_pred.fillna(False).astype(int)
            if utils.is_type(y_pred, [NumpyArray]):
                y_pred = y_pred.astype(int)
            if y is not None:
                result = metric(
                    y_true=y, y_preds=y_pred, sample_weight=sample_weight)
            else:
                result = metric(y_preds=y_pred)

            return -result

        opt_thresholds = fmin(
            fn=_objective,
            space=rule_space_funcs,
            algo=algorithm,
            max_evals=n_iter,
            verbose=verbose > 1,
            rstate=np.random.RandomState(0),
            **kwargs
        )

        # If rule_space_funcs contained constant values (due to min/max of
        # feature being equal in the dataset), then add those values back into
        # the optimised_thresholds dictionary
        if len(opt_thresholds) < len(rule_space_funcs):
            for feature, space_func in rule_space_funcs.items():
                if feature not in opt_thresholds.keys():
                    opt_thresholds[feature] = space_func
        return opt_thresholds

    @staticmethod
    def _convert_opt_int_values(opt_thresholds: Dict[str, float],
                                int_cols: List[str]) -> Dict[str, float]:
        """
        Converts threshold values based on integer columns into integer 
        format.
        """
        for feature, value in opt_thresholds.items():
            col = feature.split('%')[0]
            if col in int_cols:
                opt_thresholds[feature] = int(value)
        return opt_thresholds
