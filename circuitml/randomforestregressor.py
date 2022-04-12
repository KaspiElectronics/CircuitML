from micromlgen.utils import jinja, check_type


def is_randomforest_regressor(clf):
    """
    Test if classifier can be ported
    """
    return check_type(clf, 'RandomForestRegressor')


def port_randomforest_regressor(clf, **kwargs):
    """
    Port sklearn's RandomForestRegressor
    """
    return jinja('randomforest/randomforest_regressor.jinja', {
        'dtype': 'float',
        'n_estimators': clf.n_estimators,
        'trees': [{
            'left': clf.tree_.children_left,
            'right': clf.tree_.children_right,
            'features': clf.tree_.feature,
            'thresholds': clf.tree_.threshold,
            'values': clf.tree_.value,
        } for clf in clf.estimators_]
    }, {
        'classname': 'RandomForestRegressor'
    }, **kwargs)