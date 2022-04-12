import json
import numpy as np
from micromlgen.utils import jinja


def parse_samples(samples, parser):
    for line in samples.split('\n'):
        if '{' in line and '}' in line:
            data = json.loads(line)
            info = {k: v for k, v in data.items() if k.startswith('__')}
            networks = {k: v for k, v in data.items() if not k.startswith('__')}
            yield parser(info, networks)


def get_classmap(samples):
    """Get {location: classIdx} mapping"""

    def parser(info, networks):
        return info['__location']

    locations = list(parse_samples(samples, parser))
    return {location: i for i, location in enumerate(sorted(set(locations)))}


def get_networkmap(samples):
    """Get {network: featureIdx} mapping"""

    def parser(info, networks):
        return networks.keys()

    networks = [list(x) for x in parse_samples(samples, parser)]
    networks = [network for sub in networks for network in sub]
    return {network: i for i, network in enumerate(sorted(set(networks)))}


def get_x(samples, networkmap):
    """Get features array"""

    def parser(info, networks):
        x = [0] * len(networkmap)
        for network, rssi in networks.items():
            x[networkmap.get(network)] = rssi
        return x

    return np.asarray(list(parse_samples(samples, parser)), dtype=np.int8)


def get_y(samples, classmap):
    """Get locationIdx array"""

    def parser(info, networks):
        location = info['__location']
        assert location in classmap, 'Unknown location %s' % location
        return classmap[location]

    return np.asarray(list(parse_samples(samples, parser)))


def port_wifi_indoor_positioning(samples):
    classmap = get_classmap(samples)
    networkmap = get_networkmap(samples)
    X = get_x(samples, networkmap)
    y = get_y(samples, classmap)
    # classmap is flipped wrt the format `port` expects: flip it
    classmap = {v: k for k, v in classmap.items()}
    return X, y, classmap, jinja('wifiindoorpositioning/wifiindoorpositioning.jinja', {
        'X': X,
        'networkmap': networkmap
    })
