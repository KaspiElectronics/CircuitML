from micromlgen.utils import jinja, check_type


def is_logisticregression(clf):
    """Test if classifier can be ported"""
    return check_type(clf, 'LogisticRegression')


def port_logisticregression(clf, **kwargs):
    """Port sklearn's LogisticRegressionClassifier"""
    return jinja('logisticregression/logisticregression.jinja', {
        'weights': clf.coef_,
        'intercept': clf.intercept_,
        'classes': clf.classes_,
        'n_classes': len(clf.classes_)
    }, {
        'classname': 'LogisticRegression'
    }, **kwargs)