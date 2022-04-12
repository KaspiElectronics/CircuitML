from micromlgen.utils import jinja, check_type


def is_decisiontree_regressor(clf):
    """
    Test if classifier can be ported
    :param clf:
    :return: bool
    """
    return check_type(clf, 'DecisionTreeRegressor')


def port_decisiontree_regressor(clf, **kwargs):
    """
    Port sklearn's DecisionTreeClassifier
    :param clf:
    :return: str ported classifier
    """
    return jinja('decisiontree/decisiontree_regressor.jinja', {
        'dtype': 'float',
        'left': clf.tree_.children_left,
        'right': clf.tree_.children_right,
        'features': clf.tree_.feature,
        'thresholds': clf.tree_.threshold,
        'values': clf.tree_.value,
        'i': 0
    }, {
        'classname': 'DecisionTreeRegressor'
    }, **kwargs)