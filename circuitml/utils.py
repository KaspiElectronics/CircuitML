import os
import re
from math import sin, cos
from collections.abc import Iterable
from inspect import getmro
from jinja2 import FileSystemLoader, Environment


def check_type(instance, *classes):
    """Check if object is instance of given class"""
    for klass in classes:
        if type(instance).__name__ == klass:
            return True
        for T in getmro(type(instance)):
            if T.__name__ == klass:
                return True
    return False


def prettify(code):
    """A super simple code prettifier"""
    pretty = []
    indent = 0
    for line in code.split('\n'):
        line = line.strip()
        # skip empty lines
        if len(line) == 0:
            continue
        # lower indentation on closing braces
        if line[-1] == '}' or line == '};' or line == 'protected:':
            indent -= 1
        pretty.append(('    ' * indent) + line)
        # increase indentation on opening braces
        if line[-1] == '{' or line == 'public:' or line == 'protected:':
            indent += 1
    pretty = '\n'.join(pretty)
    # leave empty line before {return, for, if}
    pretty = re.sub(r'([;])\n(\s*?)(for|return|if) ', lambda m: '%s\n\n%s%s ' % m.groups(), pretty)
    # leave empty line after closing braces
    pretty = re.sub(r'}\n', '}\n\n', pretty)
    # strip empty lines between closing braces (2 times)
    pretty = re.sub(r'\}\n\n(\s*?)\}', lambda m: '}\n%s}' % m.groups(), pretty)
    pretty = re.sub(r'\}\n\n(\s*?)\}', lambda m: '}\n%s}' % m.groups(), pretty)
    # remove "," before "}"
    pretty = re.sub(r',\s*\}', '}', pretty)
    return pretty


def jinja(template_file, data, defaults=None, **kwargs):
    """Render Jinja template"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    loader = FileSystemLoader(dir_path + '/templates')
    template = Environment(loader=loader).get_template(template_file)
    data = {k: v for k, v in data.items() if v is not None}
    kwargs = {k: v for k, v in kwargs.items() if v is not None}
    precision = data.get('precision', 12) or 12
    precision_fmt = '%.' + str(precision) + 'f'
    if defaults is None:
        defaults = {}
    defaults.setdefault('platform', 'arduino')
    defaults.setdefault('classmap', None)
    defaults.update({
        'f': {
            'enumerate': enumerate,
            'round': lambda x: round(x, precision),
            'zip': zip,
            'signed': lambda x: '' if x == 0 else '+' + str(x) if x >= 0 else x,
            'to_array': lambda x, as_int=False: ', '.join([precision_fmt % xx if not as_int else str(xx) for xx in x])
        },
        'math': {
            'cos': cos,
            'sin': sin
        }
    })
    data = {
        **defaults,
        **kwargs,
        **data
    }
    code = template.render(data)
    return prettify(code)


def port_trainset(X, y, classname='TrainSet'):
    return jinja('trainset.jinja', locals())


def port_testset(X, y, classname='TestSet'):
    return jinja('testset.jinja', locals())


def port_array(arr, precision=9):
    """
    Convert array to C
    :param arr: list|ndarray
    :param precision: int how many decimal digits to print
    :return: str C-array contents
    """
    if not isinstance(arr, Iterable):
        fmt = '%%.%df' % precision
        return fmt % arr

    return '{%s}' % (', '.join([port_array(x, precision) for x in arr]))