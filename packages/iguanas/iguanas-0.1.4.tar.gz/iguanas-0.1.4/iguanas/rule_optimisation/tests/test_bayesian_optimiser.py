from iguanas.rule_optimisation import BayesianOptimiser
from iguanas.metrics import FScore, AlertsPerDay
from iguanas.rules import Rules
from iguanas.warnings import RulesNotOptimisedWarning
from iguanas.exceptions import RulesNotOptimisedError
import pytest
import numpy as np
import pandas as pd
from hyperopt import hp, tpe
from hyperopt.pyll import scope


@pytest.fixture
def _create_data():
    np.random.seed(0)
    X = pd.DataFrame({
        'A': np.random.randint(0, 10, 10000),
        'B': np.random.randint(0, 100, 10000),
        'C': np.random.uniform(0, 1, 10000),
        'D': [True, False] * 5000,
        'E': ['yes', 'no'] * 5000,
        'AllNa': [np.nan] * 10000,
        'ZeroVar': [1] * 10000
    })
    X.loc[10000] = [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
    X['A'] = X['A'].astype('Int64')
    X['B'] = X['B'].astype('Int64')
    X['D'] = X['D'].astype('boolean')
    y = pd.Series(np.random.randint(0, 2, 10001))
    sample_weight = pd.Series(
        np.where((X['A'] > 7).fillna(False) & (y == 0), 100, 1))
    return X, y, sample_weight


@pytest.fixture
def _create_inputs():
    rule_lambdas = {
        'integer': lambda **kwargs: "(X['A']>{A})".format(**kwargs),
        'float': lambda **kwargs: "(X['C']>{C})".format(**kwargs),
        'categoric': lambda **kwargs: "(X['E']=='yes')".format(**kwargs),
        'boolean': lambda **kwargs: "(X['D']==True)".format(**kwargs),
        'is_na': lambda **kwargs: "(X['A']>{A})|(X['A'].isna())".format(**kwargs),
        'mixed': lambda **kwargs: "((X['A']>{A})&(X['C']>{C})&(X['E']=='yes')&(X['D']==True))|(X['C']>{C%0})".format(**kwargs),
        'missing_col': lambda **kwargs: "(X['Z']>{Z})".format(**kwargs),
        'all_na': lambda **kwargs: "(X['AllNa']>{AllNa})".format(**kwargs),
        'zero_var': lambda **kwargs: "(X['ZeroVar']>{ZeroVar})".format(**kwargs),
        'already_optimal': lambda **kwargs: "(X['A']>={A})".format(**kwargs),
        'float_with_zero_var': lambda **kwargs: "(X['C']>{C})&(X['ZeroVar']>={ZeroVar})".format(**kwargs),
        'float_with_all_na_greater': lambda **kwargs: "(X['C']>{C})&(X['AllNa']>{AllNa})".format(**kwargs),
        'float_with_all_na_is_na': lambda **kwargs: "(X['C']>{C})&(X['AllNa'].isna())".format(**kwargs),
        'multi_zero_var': lambda **kwargs: "((X['C']>{C})&(X['ZeroVar']>={ZeroVar}))|((X['A']>{A})&(X['ZeroVar']>={ZeroVar%0}))".format(**kwargs),
    }
    lambda_kwargs = {
        'integer': {'A': 9},
        'float': {'C': 1.5},
        'categoric': {},
        'boolean': {},
        'is_na': {'A': 9},
        'mixed': {'A': 1, 'C': 1.5, 'C%0': 2.5},
        'missing_col': {'Z': 1},
        'all_na': {'AllNa': 5},
        'zero_var': {'ZeroVar': 1},
        'already_optimal': {'A': 0},
        'float_with_zero_var': {'C': 1.5, 'ZeroVar': 1},
        'float_with_all_na_greater': {'C': 1.5, 'AllNa': 1},
        'float_with_all_na_is_na': {'C': 1.5},
        'multi_zero_var': {'C': 1.5, 'ZeroVar': 1, 'A': 9, 'ZeroVar%0': 1}
    }
    return rule_lambdas, lambda_kwargs


@pytest.fixture
def _expected_results():
    opt_rule_strings = {
        'integer': "(X['A']>0)",
        'float': "(X['C']>0.003230558992660632)",
        'is_na': "(X['A']>0)|(X['A'].isna())",
        'mixed': "((X['A']>8)&(X['C']>0.2731178395058975)&(X['E']=='yes')&(X['D']==True))|(X['C']>0.003230558992660632)",
        'already_optimal': "(X['A']>=0)",
        'float_with_zero_var': "(X['C']>0.003230558992660632)&(X['ZeroVar']>=1)",
        'float_with_all_na_greater': "(X['C']>1.5)&(X['AllNa']>1)",
        'float_with_all_na_is_na': "(X['C']>0.003230558992660632)&(X['AllNa'].isna())",
        'multi_zero_var': "((X['C']>0.001111407676385845)&(X['ZeroVar']>=1))|((X['A']>3)&(X['ZeroVar']>=1))",
        'categoric': "(X['E']=='yes')",
        'boolean': "(X['D']==True)"
    }
    opt_rule_strings_weighted = {
        'integer': "(X['A']>0)",
        'float': "(X['C']>0.14437974242018892)",
        'is_na': "(X['A']>0)|(X['A'].isna())",
        'mixed': "((X['A']>3)&(X['C']>0.3449413915707924)&(X['E']=='yes')&(X['D']==True))|(X['C']>0.14437974242018892)",
        'already_optimal': "(X['A']>=0)",
        'float_with_zero_var': "(X['C']>0.14437974242018892)&(X['ZeroVar']>=1)",
        'float_with_all_na_greater': "(X['C']>1.5)&(X['AllNa']>1)",
        'float_with_all_na_is_na': "(X['C']>0.14437974242018892)&(X['AllNa'].isna())",
        'multi_zero_var': "((X['C']>0.003230558992660632)&(X['ZeroVar']>=1))|((X['A']>2)&(X['ZeroVar']>=1))",
        'categoric': "(X['E']=='yes')",
        'boolean': "(X['D']==True)"
    }
    orig_rule_performances = {
        'already_optimal': 0.6657771847898598,
        'integer': 0.0,
        'float': 0.0,
        'is_na': 0.0,
        'mixed': 0.0,
        'float_with_zero_var': 0.0,
        'float_with_all_na_greater': 0.0,
        'float_with_all_na_is_na': 0.0,
        'multi_zero_var': 0.0
    }
    orig_rule_performances_weighted = {
        'already_optimal': 0.08504038992467365,
        'integer': 0.0,
        'float': 0.0,
        'is_na': 0.0,
        'mixed': 0.0,
        'float_with_zero_var': 0.0,
        'float_with_all_na_greater': 0.0,
        'float_with_all_na_is_na': 0.0,
        'multi_zero_var': 0.0
    }
    opt_rule_performances = {
        'float': 0.6642155224279698,
        'mixed': 0.6642155224279698,
        'integer': 0.6422306211224418,
        'already_optimal': 0.6657771847898598,
        'is_na': 0.6421848260125499,
        'float_with_zero_var': 0.6642155224279698,
        'float_with_all_na_greater': 0.0,
        'float_with_all_na_is_na': 0.6642155224279698,
        'multi_zero_var': 0.6655101087609262
    }
    opt_rule_performances_weighted = {
        'float': 0.0864948723631455,
        'mixed': 0.0864948723631455,
        'integer': 0.07737844641675759,
        'already_optimal': 0.08504038992467365,
        'is_na': 0.07737778159635708,
        'float_with_zero_var': 0.0864948723631455,
        'float_with_all_na_greater': 0.0,
        'float_with_all_na_is_na': 0.0864948723631455,
        'multi_zero_var': 0.08491056439448814
    }
    return opt_rule_strings, opt_rule_strings_weighted, orig_rule_performances, \
        orig_rule_performances_weighted, opt_rule_performances, opt_rule_performances_weighted


@pytest.fixture
def _expected_X_rules_mean():
    X_rules_no_weight = pd.Series(
        {
            'already_optimal': 0.99990001,
            'float': 0.9968003199680032,
            'mixed': 0.9968003199680032,
            'integer': 0.9032096790320968,
            'is_na': 0.9033096690330967,
            'float_with_zero_var': 0.99680,
            'float_with_all_na_greater': 0.00000,
            'float_with_all_na_is_na': 0.99680,
            'multi_zero_var': 0.99960,
            'categoric': 0.49995,
            'boolean': 0.49995
        },
    )
    X_rules_weight = pd.Series(
        {
            'float': 0.8541145885411459,
            'mixed': 0.8541145885411459,
            'already_optimal': 0.99990001,
            'integer': 0.9032096790320968,
            'is_na': 0.9033096690330967,
            'float_with_zero_var': 0.8541145885411459,
            'float_with_all_na_greater': 0.0,
            'float_with_all_na_is_na': 0.8541145885411459,
            'multi_zero_var': 0.999000099990001,
            'categoric': 0.49995000499950004,
            'boolean': 0.49995000499950004
        },
    )
    X_rules_unlab = pd.Series(
        {
            'float': 0.0059994000599940004,
            'mixed': 0.0,
            'integer': 0.0,
            'is_na': 9.999000099990002e-05,
            'already_optimal': 0.209179,
            'float_with_zero_var': 0.0059994000599940004,
            'float_with_all_na_greater': 0.0,
            'float_with_all_na_is_na': 0.0059994000599940004,
            'multi_zero_var': 0.0,
            'categoric': 0.49995000499950004,
            'boolean': 0.49995000499950004
        },
    )
    return X_rules_no_weight, X_rules_weight, X_rules_unlab


@pytest.fixture
def _expected_results_unlabelled():
    opt_rule_strings = {
        'integer': "(X['A']>9)",
        'float': "(X['C']>0.9934712038306385)",
        'is_na': "(X['A']>9)|(X['A'].isna())",
        'mixed': "((X['A']>1)&(X['C']>1.5)&(X['E']=='yes')&(X['D']==True))|(X['C']>2.5)",
        'already_optimal': "(X['A']>=8)",
        'float_with_zero_var': "(X['C']>0.9934712038306385)&(X['ZeroVar']>=1)",
        'float_with_all_na_greater': "(X['C']>1.5)&(X['AllNa']>1)",
        'float_with_all_na_is_na': "(X['C']>0.9934712038306385)&(X['AllNa'].isna())",
        'multi_zero_var': "((X['C']>1.5)&(X['ZeroVar']>=1))|((X['A']>9)&(X['ZeroVar']>=1))",
        'categoric': "(X['E']=='yes')",
        'boolean': "(X['D']==True)"
    }
    orig_rule_performances = {
        'is_na': -98.01,
        'integer': -100.0,
        'float': -100.0,
        'mixed': -100.0,
        'already_optimal': -980100.0,
        'float_with_zero_var': -100.0,
        'float_with_all_na_greater': -100.0,
        'float_with_all_na_is_na': -100.0,
        'multi_zero_var': -100.0
    }
    opt_rule_performances = {
        'float': -16.0,
        'mixed': -100.0,
        'integer': -100.0,
        'is_na': -98.01,
        'already_optimal': -39680.63999999999,
        'float_with_zero_var': -16.0,
        'float_with_all_na_greater': -100.0,
        'float_with_all_na_is_na': -16.0,
        'multi_zero_var': -100.0
    }
    return opt_rule_strings, orig_rule_performances, opt_rule_performances


@pytest.fixture
def _instantiate(_create_inputs):
    rule_lambdas, lambda_kwargs = _create_inputs
    f1 = FScore(beta=1)
    ro = BayesianOptimiser(
        rule_lambdas=rule_lambdas,
        lambda_kwargs=lambda_kwargs,
        metric=f1.fit,
        n_iter=30,
        num_cores=2,
        verbose=2
    )
    return ro


def test_fit_and_fit_transform(_create_data, _instantiate, _expected_results, _expected_X_rules_mean):
    X, y, _ = _create_data
    exp_opt_rule_strings, _, exp_orig_rule_performances, _, exp_opt_rule_performances, _ = _expected_results
    exp_X_rules, _, _ = _expected_X_rules_mean
    ro = _instantiate
    assert ro.__repr__() == 'BayesianOptimiser object with 14 rules to optimise'
    with pytest.warns(RulesNotOptimisedWarning) as warnings:
        for method in ['fit', 'fit_transform']:
            if method == 'fit':
                X_rules = ro.fit(X=X, y=y)
            else:
                X_rules = ro.fit_transform(X=X, y=y)
            assert ro.__repr__() == 'BayesianOptimiser object with 9 optimised rules and 2 unoptimisable rules'
            pd.testing.assert_series_equal(
                X_rules.mean().sort_index(), exp_X_rules.sort_index()
            )
            assert ro.rule_strings == ro.rules.rule_strings == exp_opt_rule_strings
            assert ro.rule_names == list(exp_opt_rule_strings.keys())
            assert ro.orig_rule_performances == exp_orig_rule_performances
            assert ro.opt_rule_performances == exp_opt_rule_performances
            assert ro.rule_names_missing_features == ['missing_col']
            assert ro.rule_names_no_opt_conditions == ['categoric', 'boolean']
            assert ro.rule_names_zero_var_features == ['all_na', 'zero_var']
    # Assert warnings
    warnings = [w.message.args[0] for w in warnings]
    assert 'Rules `missing_col` use features that are missing from `X` - unable to optimise or apply these rules' in warnings
    assert 'Rules `categoric`, `boolean` have no optimisable conditions - unable to optimise these rules' in warnings
    assert 'Rules `all_na`, `zero_var` have all zero variance features based on the dataset `X` - unable to optimise these rules' in warnings


def test_fit_weighted(_create_data, _instantiate, _expected_results,
                      _expected_X_rules_mean):
    X, y, sample_weight = _create_data
    _, exp_opt_rule_strings, _, exp_orig_rule_performances, _, exp_opt_rule_performances = _expected_results
    _, exp_X_rules, _ = _expected_X_rules_mean
    ro = _instantiate
    with pytest.warns(RulesNotOptimisedWarning) as warnings:
        X_rules = ro.fit(X=X, y=y, sample_weight=sample_weight)
        pd.testing.assert_series_equal(
            X_rules.mean().sort_index(), exp_X_rules.sort_index())
        assert ro.rule_strings == ro.rules.rule_strings == exp_opt_rule_strings
        assert ro.rule_names == list(exp_opt_rule_strings.keys())
        assert ro.orig_rule_performances == exp_orig_rule_performances
        assert ro.opt_rule_performances == exp_opt_rule_performances
        assert ro.rule_names_missing_features == ['missing_col']
        assert ro.rule_names_no_opt_conditions == [
            'categoric', 'boolean']
        assert ro.rule_names_zero_var_features == ['all_na', 'zero_var']
        # Assert warnings
        warnings = [w.message.args[0] for w in warnings]
        assert 'Rules `missing_col` use features that are missing from `X` - unable to optimise or apply these rules' in warnings
        assert 'Rules `categoric`, `boolean` have no optimisable conditions - unable to optimise these rules' in warnings
        assert 'Rules `all_na`, `zero_var` have all zero variance features based on the dataset `X` - unable to optimise these rules' in warnings


def test_fit_unlabelled(_create_data, _instantiate,
                        _expected_results_unlabelled, _expected_X_rules_mean):
    X, _, _ = _create_data
    exp_opt_rule_strings, exp_orig_rule_performances, exp_opt_rule_performances = _expected_results_unlabelled
    _, _, exp_X_rules = _expected_X_rules_mean
    apd = AlertsPerDay(n_alerts_expected_per_day=10, no_of_days_in_file=10)
    ro = _instantiate
    ro.metric = apd.fit
    with pytest.warns(RulesNotOptimisedWarning) as warnings:
        X_rules = ro.fit(X=X)
        pd.testing.assert_series_equal(
            X_rules.mean().sort_index(), exp_X_rules.sort_index())
        assert ro.rule_strings == ro.rules.rule_strings == exp_opt_rule_strings
        assert ro.rule_names == list(exp_opt_rule_strings.keys())
        assert ro.orig_rule_performances == exp_orig_rule_performances
        assert ro.opt_rule_performances == exp_opt_rule_performances
        assert ro.rule_names_missing_features == ['missing_col']
        assert ro.rule_names_no_opt_conditions == ['categoric', 'boolean']
        assert ro.rule_names_zero_var_features == ['all_na', 'zero_var']
        # Assert warnings
        warnings = [w.message.args[0] for w in warnings]
        assert 'Rules `missing_col` use features that are missing from `X` - unable to optimise or apply these rules' in warnings
        assert 'Rules `categoric`, `boolean` have no optimisable conditions - unable to optimise these rules' in warnings
        assert 'Rules `all_na`, `zero_var` have all zero variance features based on the dataset `X` - unable to optimise these rules' in warnings


def test_transform(_instantiate):
    ro = _instantiate
    X = pd.DataFrame({
        'A': [1, 2, 0, 1, 0, 2]
    })
    exp_X_rules = pd.DataFrame({
        'Rule': [0, 1, 0, 0, 0, 1]
    })
    ro.rule_strings = {'Rule': "(X['A']>1)"}
    X_rules = ro.transform(X)
    np.testing.assert_array_equal(X_rules.values, exp_X_rules.values)


def test_optimise_rules(_create_data, _instantiate, _expected_results):
    X, y, sample_weight = _create_data
    ro = _instantiate
    exp_opt_rule_strings, exp_opt_rule_strings_weighted, _, _, _, _ = _expected_results
    for rule_name in ['missing_col', 'categoric', 'boolean', 'all_na', 'zero_var', 'already_optimal']:
        ro.orig_rule_lambdas.pop(rule_name)
        ro.orig_lambda_kwargs.pop(rule_name)
        exp_opt_rule_strings.pop(rule_name, None)
        exp_opt_rule_strings_weighted.pop(rule_name, None)
    int_cols = ['A', 'B', 'D']
    all_space_funcs = {
        'A': scope.int(hp.uniform('A', X['A'].min(), X['A'].max())),
        'C%0': hp.uniform('C%0', X['C'].min(), X['C'].max()),
        'C': hp.uniform('C', X['C'].min(), X['C'].max()),
        'ZeroVar': 1,
        'ZeroVar%0': 1,
        'AllNa': 0
    }
    # Update optimised rule_strings for float_with_all_na_greater, since
    # optimiser outputs rule string with same performance as original
    exp_opt_rule_strings['float_with_all_na_greater'] = "(X['C']>0.4862189294416758)&(X['AllNa']>0)"
    exp_opt_rule_strings_weighted[
        'float_with_all_na_greater'] = "(X['C']>0.4862189294416758)&(X['AllNa']>0)"
    # Add verbose = 1 to test utils.return_progress_ready_range
    ro.verbose = 1
    for exp_result, w in zip([exp_opt_rule_strings, exp_opt_rule_strings_weighted], [None, sample_weight]):
        opt_rule_strings = ro._optimise_rules(
            rule_lambdas=ro.orig_rule_lambdas,
            lambda_kwargs=ro.orig_lambda_kwargs,
            X=X, y=y, sample_weight=w,
            int_cols=int_cols, all_space_funcs=all_space_funcs
        )
        assert opt_rule_strings == exp_result


def test_optimise_single_rule(_create_inputs, _instantiate, _create_data, _expected_results):
    rule_lambdas, lambda_kwargs = _create_inputs
    X, y, _ = _create_data
    exp_opt_rule_strings, _, _, _, _, _ = _expected_results
    ro = _instantiate
    int_cols = ['A']
    all_space_funcs = {
        'A': scope.int(hp.uniform('A', X['A'].min(), X['A'].max())),
        'C%0': hp.uniform('C%0', X['C'].min(), X['C'].max()),
        'C': hp.uniform('C', X['C'].min(), X['C'].max())
    }
    for rule_name in ['integer', 'float', 'is_na', 'mixed']:
        opt_rule_string = ro._optimise_single_rule(
            rule_name=rule_name, rule_lambda=rule_lambdas[rule_name],
            lambda_kwargs=lambda_kwargs, X=X, y=y, sample_weight=None,
            int_cols=int_cols, all_space_funcs=all_space_funcs)
        assert rule_name, exp_opt_rule_strings[rule_name] == opt_rule_string


def test_return_int_cols(_instantiate):
    exp_int_cols = ['int', 'int_stored_as_float']
    X = pd.DataFrame({
        'int': [0, 1, 2, np.nan],
        'float': [0, 1.5, 2.5, np.nan],
        'int_stored_as_float': [1, 2, 3, np.nan]
    })
    X['int'] = X['int'].astype('Int64')
    ro = _instantiate
    int_cols = ro._return_int_cols(X=X)
    assert int_cols == exp_int_cols


def test_return_all_space_funcs(_create_data, _instantiate):
    X, _, _ = _create_data
    exp_results = {
        'A': 'int',
        'C': 'float',
        'C%0': 'float'
    }
    ro = _instantiate
    all_rule_features = ['A', 'C', 'C%0']
    int_cols = ['A']
    X_min = X.min()
    X_max = X.max()
    space_funcs = ro._return_all_space_funcs(
        rule_features_set_tagged=all_rule_features,
        X_min=X_min,
        X_max=X_max,
        int_cols=int_cols)
    for rule_name, space_func in space_funcs.items():
        assert space_func.name == exp_results[rule_name]


def test_return_rule_space_funcs(_instantiate):
    all_space_funcs = {
        'A': 'FuncA',
        'B': 'FuncB',
        'C': 'FuncC'
    }
    exp_result = {
        'A': 'FuncA',
        'C': 'FuncC'
    }
    rule_features = ['A', 'C']
    ro = _instantiate
    rule_space_funcs = ro._return_rule_space_funcs(
        all_space_funcs=all_space_funcs, rule_features=rule_features)
    assert rule_space_funcs == exp_result


def test_optimise_rule_thresholds(_create_data, _create_inputs, _instantiate):
    exp_opt_threshold = {'A': 0.8284904721469425}
    f1 = FScore(beta=1)
    X, y, sample_weight = _create_data
    rule_lambdas, _ = _create_inputs
    rule_lambda = rule_lambdas['integer']
    rule_space_funcs = {
        'A': scope.int(hp.uniform('A', X['A'].min(), X['A'].max())),
    }
    ro = _instantiate
    for w in [None, sample_weight]:
        opt_threshold = ro._optimise_rule_thresholds(
            rule_lambda=rule_lambda, rule_space_funcs=rule_space_funcs, X_=X,
            y=y, sample_weight=w, metric=f1.fit, n_iter=30, verbose=0,
            algorithm=tpe.suggest, kwargs={})
        assert opt_threshold == exp_opt_threshold


def test_optimise_rule_thresholds_unlabelled(_create_data, _create_inputs, _instantiate):
    exp_opt_threshold = {'A': 8.704181023958697}
    apd = AlertsPerDay(n_alerts_expected_per_day=10, no_of_days_in_file=10)
    X, y, _ = _create_data
    rule_lambdas, _ = _create_inputs
    rule_lambda = rule_lambdas['integer']
    rule_space_funcs = {
        'A': scope.int(hp.uniform('A', X['A'].min(), X['A'].max())),
    }
    ro = _instantiate
    opt_threshold = ro._optimise_rule_thresholds(
        rule_lambda=rule_lambda, rule_space_funcs=rule_space_funcs, X_=X,
        y=None, sample_weight=None, metric=apd.fit, n_iter=30, verbose=0,
        algorithm=tpe.suggest, kwargs={})
    assert opt_threshold == exp_opt_threshold


def test_optimise_rule_thresholds_zero_var_feat(_create_data, _instantiate):
    rule_strings = {
        'Rule1': "((X['A']>9)&(X['ZeroVar']>0))|(X['A'].isna())"
    }
    rule = Rules(rule_strings=rule_strings)
    rule_lambdas = rule.as_rule_lambdas(as_numpy=True, with_kwargs=True)
    rule_lambda = rule_lambdas['Rule1']
    exp_opt_threshold = {'A': 4.374425907193953, 'ZeroVar': 1}
    f1 = FScore(beta=1)
    X, y, _ = _create_data
    rule_space_funcs = {
        'A': scope.int(hp.uniform('A', X['A'].min(), X['A'].max())),
        'ZeroVar': 1
    }
    ro = _instantiate
    opt_threshold = ro._optimise_rule_thresholds(
        rule_lambda=rule_lambda, rule_space_funcs=rule_space_funcs, X_=X,
        y=y, sample_weight=None, metric=f1.fit, n_iter=30, verbose=0,
        algorithm=tpe.suggest, kwargs={})
    assert opt_threshold == exp_opt_threshold


def test_convert_opt_int_values(_instantiate):
    exp_result = {
        'A': 0,
        'C%0': 1.2,
        'C': 2
    }
    opt_thresholds = {
        'A': 0.82,
        'C%0': 1.2,
        'C': 2
    }
    int_cols = ['A']
    ro = _instantiate
    opt_thresholds = ro._convert_opt_int_values(
        opt_thresholds=opt_thresholds, int_cols=int_cols)
    assert opt_thresholds == exp_result


def test_errors(_create_data, _instantiate):
    X, y, _ = _create_data
    ro = _instantiate
    with pytest.raises(TypeError, match='`X` must be a pandas.core.frame.DataFrame. Current type is list.'):
        ro.fit(X=[], y=y)
    with pytest.raises(TypeError, match='`y` must be a pandas.core.series.Series. Current type is list.'):
        ro.fit(X=X, y=[])
    with pytest.raises(TypeError, match='`sample_weight` must be a pandas.core.series.Series. Current type is list.'):
        ro.fit(X=X, y=y, sample_weight=[])
    X = pd.DataFrame({'ZeroVar': [0, 0, 0]})
    y = pd.Series([0, 1, 0])
    with pytest.warns(RulesNotOptimisedWarning, match="Rules `integer`, `float`, `categoric`, `boolean`, `is_na`, `mixed`, `missing_col`, `all_na`, `already_optimal`, `float_with_zero_var`, `float_with_all_na_greater`, `float_with_all_na_is_na`, `multi_zero_var` use features that are missing from `X` - unable to optimise or apply these rules"):
        with pytest.raises(RulesNotOptimisedError, match='There are no optimisable rules in the set'):
            ro.fit(X=X, y=y)
