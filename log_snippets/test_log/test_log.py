import logging

from log_snippets.configuration_methods import log_util as lu

log = logging.getLogger(__name__)


def say_bye():
    log.debug('say bye')


if __name__ == '__main__':
    lu.print_hello()
    say_bye()
    log.debug('completed ')
    log.info('just information')
