from micromlgen.utils import jinja, check_type


def is_sefr(clf):
    """Test if classifier can be ported"""
    return check_type(clf, 'SEFR')


def port_sefr(clf, classname=None, **kwargs):
    """Port SEFR classifier"""
    return jinja('sefr/sefr.jinja', {
        'weights': clf.weights,
        'bias': clf.bias,
        'dimension': len(clf.weights),
    }, {
        'classname': 'SEFR'
    }, **kwargs)