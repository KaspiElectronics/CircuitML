from micromlgen.utils import jinja, check_type


def is_gaussiannb(clf):
    """Test if classifier can be ported"""
    return check_type(clf, 'GaussianNB')


def port_gaussiannb(clf, **kwargs):
    """Port sklearn's GaussianNB"""
    return jinja('gaussiannb/gaussiannb.jinja', {
        'sigma': clf.sigma_,
        'theta': clf.theta_,
        'prior': clf.class_prior_,
        'classes': clf.classes_,
        'n_classes': len(clf.classes_)
    }, {
        'classname': 'GaussianNB'
    }, **kwargs)