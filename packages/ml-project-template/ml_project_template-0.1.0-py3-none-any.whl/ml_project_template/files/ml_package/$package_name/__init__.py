from $package_name.config import config, logging_config
import logging

# Configure logger for use in package
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_config.get_console_handler())
logger.propagate = False

VERSION_PATH = config.PACKAGE_ROOT / 'VERSION'

with open(VERSION_PATH, 'r') as version_file:
    __version__ = version_file.read().strip()