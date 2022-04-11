from micromlgen.utils import jinja, check_type


def is_randomforest(clf):
    """Test if classifier can be ported"""
    return check_type(clf, 'RandomForestClassifier')


def port_randomforest(clf, **kwargs):
    """Port sklearn's RandomForestClassifier"""
    return jinja('randomforest/randomforest.jinja', {
        'n_classes': clf.n_classes_,
        'trees': [{
            'left': clf.tree_.children_left,
            'right': clf.tree_.children_right,
            'features': clf.tree_.feature,
            'thresholds': clf.tree_.threshold,
            'classes': clf.tree_.value,
        } for clf in clf.estimators_]
    }, {
        'classname': 'RandomForest'
    }, **kwargs)