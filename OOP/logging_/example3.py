import logging
import os
import tomllib


with open(os.path.join("..", "..", "logging.toml"), mode='rb') as f:
    config = tomllib.load(f)

logging.config.dictConfig(config)

logger = logging.getLogger("my_logger")
logger.info("Info message")
logger.debug("Debug message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")

