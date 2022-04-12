from micromlgen.utils import jinja, check_type


def is_pca(clf):
    """Test if classifier can be ported"""
    return check_type(clf, 'PCA')


def port_pca(clf, **kwargs):
    """Port a PCA"""
    return jinja('pca/pca.jinja', {
        'arrays': {
            'components': clf.components_,
            'mean': clf.mean_
        },
    }, {
        'classname': 'PCA'
    }, **kwargs)