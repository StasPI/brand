import pathlib

import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
# Potential problem with defining base directory. Just remove / 'brand' /
config_path = BASE_DIR / 'brand' / 'config' / 'config.yaml'

#docker
# config_path = BASE_DIR / 'app' / 'config' / 'config.yaml'


'''
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Extracting data from a config file
'''


def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config


config = get_config(config_path)
