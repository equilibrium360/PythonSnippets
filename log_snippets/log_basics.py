# import logging as log

# root is the default logger
# For practical purposes we don't use root logger
# we need to create custom logger
log.basicConfig(
    filename='app.log',
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s'
)

log.warning('first long msg')

# Define custom logger

logger = log.getLogger(__name__)
logger.info("Custom Logger message")
