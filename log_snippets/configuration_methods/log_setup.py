import logging.config

import yaml

with open('/Users/UNIVERSE/PycharmProjects/PythonSnippets/log_snippets/configuration_methods/log_config.yaml',
          'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
