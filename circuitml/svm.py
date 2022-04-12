from micromlgen.utils import jinja, check_type


def is_svm(clf):
    """Test if classifier can be ported"""
    return check_type(clf, 'SVC', 'OneClassSVM')


def port_svm(clf, **kwargs):
    """Port a SVC / OneClassSVC classifier"""
    assert isinstance(clf.gamma, float), 'You probably didn\'t set an explicit value for gamma: 0.001 is a good default'

    support_v = clf.support_vectors_
    n_classes = len(clf.n_support_)

    return jinja('svm/svm.jinja', {
        'kernel': {
            'type': clf.kernel,
            'gamma': clf.gamma,
            'coef0': clf.coef0,
            'degree': clf.degree
        },
        'sizes': {
            'features': len(support_v[0]),
            'vectors': len(support_v),
            'classes': n_classes,
            'decisions': n_classes * (n_classes - 1) // 2,
            'supports': clf.n_support_
        },
        'arrays': {
            'supports': support_v,
            'intercepts': clf.intercept_,
            'coefs': clf.dual_coef_
        }
    }, {
        'classname': 'OneClassSVM' if check_type(clf, 'OneClassSVM') else 'SVM'
    }, **kwargs)