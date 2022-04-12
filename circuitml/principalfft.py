from micromlgen.utils import jinja, check_type
from math import pi


def is_principalfft(clf):
    """Test if classifier can be ported"""
    return check_type(clf, 'PrincipalFFT') or check_type(clf, 'KFFT')


def port_principalfft(clf, optimize_sin=False, lookup_cos=None, lookup_sin=None, **kwargs):
    """Port PrincipalFFT classifier"""
    return jinja('principalfft/principalfft.jinja', {
        'fft': clf,
        'PI': pi,
        'size': len(clf.idx),
        'optmize_sin': optimize_sin,
        'lookup_cos': lookup_cos,
        'lookup_sin': lookup_sin,
    }, **kwargs)