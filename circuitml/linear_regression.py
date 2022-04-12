from micromlgen.utils import jinja, check_type


def is_linear_regression(clf):
    """Test if classifier can be ported"""
    return check_type(clf, 'LinearRegression')


def port_linear_regression(clf, classname=None, **kwargs):
    """Port Linear Regression"""
    return jinja('linearregression/linearregression.jinja', {
        'coefs': clf.coef_,
        'intercept': clf.intercept_,
        'dimension': len(clf.coef_),
        'dtype': 'float'
    }, {
        'classname': 'LinearRegression'
    }, **kwargs)