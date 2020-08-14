import logging.config
import logging.config

import yaml

with open('log_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger('sampleLogger')

logger.debug('This is a debug  message')
print('sss' + __name__)
