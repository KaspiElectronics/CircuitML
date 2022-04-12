from micromlgen.utils import jinja, check_type


def is_decisiontree(clf):
    """Test if classifier can be ported"""
    return check_type(clf, 'DecisionTreeClassifier')


def port_decisiontree(clf, **kwargs):
    """Port sklearn's DecisionTreeClassifier"""
    return jinja('decisiontree/decisiontree.jinja', {
        'left': clf.tree_.children_left,
        'right': clf.tree_.children_right,
        'features': clf.tree_.feature,
        'thresholds': clf.tree_.threshold,
        'classes': clf.tree_.value,
        'i': 0
    }, {
        'classname': 'DecisionTree'
    }, **kwargs)