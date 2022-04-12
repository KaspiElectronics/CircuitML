from micromlgen.utils import jinja, check_type


def is_rvm(clf):
    """Test if classifier can be ported"""
    return check_type(clf, 'RVC')


def port_rvm(clf, **kwargs):
    """Port a RVM classifier"""
    return jinja('rvm/rvm.jinja', {
        'n_classes': len(clf.intercept_),
        'kernel': {
            'type': clf.kernel,
            'gamma': clf.gamma,
            'coef0': clf.coef0,
            'degree': clf.degree
        },
        'sizes': {
            'features': clf.relevant_vectors_[0].shape[1],
        },
        'arrays': {
            'vectors': clf.relevant_vectors_,
            'coefs': clf.coef_,
            'actives': clf.active_,
            'intercepts': clf.intercept_,
            'mean': clf._x_mean,
            'std': clf._x_std
        },
    }, {
        'classname': 'RVC'
    }, **kwargs)
