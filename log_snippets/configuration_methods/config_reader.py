import logging.config

import yaml


def print_module_name():
    print("module name is " + __name__)


def load_log_config():
    with open('log_config.yaml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    print('aaaaaaaaaa')


print('sss' + __name__)
if __name__ == '__main__':
    load_log_config()
    print_module_name()
    log = logging.getLogger(__name__)
    logger = logging.getLogger('sampleLogger')
    logger.debug('This is a debug message')
    print('helo')
    log.debug('This is a root debug message')
