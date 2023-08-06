"""Class for accessing a class attribute within a pipeline."""
from typing import Union, Dict


class ClassAccessor:

    """
    Extracts a class attribute from a class (which is specified by a class 
    tag). This is used as a parameter for classes instantiated in an Iguanas
    pipeline - this allows attributes from classes that are configured earlier 
    in the pipeline to be passed to a class that appears later in the pipeline.

    Parameters
    ----------
    class_tag : str
        The tag corresponding to the class where the attribute is located.
    class_attribute : str
        The name of the attribute to be extracted.    

    Examples
    --------
    >>> from iguanas.pipeline import LinearPipeline, ClassAccessor
    >>> from iguanas.rule_generation import RuleGeneratorDT
    >>> from iguanas.metrics import FScore
    >>> from sklearn.ensemble import RandomForestClassifier
    >>> import pandas as pd
    >>> X = pd.DataFrame({
    ...     'A': [1, 0, 1, 0],
    ...     'B': [1, 1, 1, 0]
    ... })
    >>> y = pd.Series([
    ...     1, 0, 1, 0
    ... ])
    >>> f1 = FScore(beta=1)
    >>> rg = RuleGeneratorDT(
    ...     metric=f1.fit, 
    ...     n_total_conditions=2, 
    ...     tree_ensemble=RandomForestClassifier(random_state=0), 
    ...     rule_name_prefix='Rule'
    ... )
    >>> lp = LinearPipeline(
    ...     steps=[
    ...         ('rg', rg)
    ...     ]
    ... )
    >>> lp.fit(X=X, y=y)
    >>> pipeline_params = lp.get_params()
    >>> ca = ClassAccessor(
    ...     class_tag='rg', 
    ...     class_attribute='rule_names'
    ... )
    >>> print(ca.get(pipeline_params=pipeline_params))
    ['Rule_0', 'Rule_1', 'Rule_2']
    """

    def __init__(self,
                 class_tag: str,
                 class_attribute: str) -> None:

        self.class_tag = class_tag
        self.class_attribute = class_attribute

    def get(self,
            pipeline_params: Dict[str, dict]) -> Union[str, float, int, dict, list, tuple]:
        """
        Extracts the given class attribute.

        Parameters
        ----------
        pipeline_params : Dict[str, dict]
            The parameters of the pipeline containing the class attribute.

        Returns
        -------
        Union[str, float, int, dict, list, tuple]
            The class attribute.

        Raises
        ------
        ValueError
            If the `class_tag` cannot be found in `steps`.
        """

        if self.class_tag in pipeline_params.keys():
            return pipeline_params[self.class_tag][self.class_attribute]
        raise ValueError(
            f"There are no steps in `pipeline` corresponding to `class_tag`='{self.class_tag}'"
        )
