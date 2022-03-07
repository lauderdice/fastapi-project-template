"""
File for storing functions related to the set up of the project
- logging
- environment variable setup
"""

import logging
import os
from logging import Formatter
from dotenv import load_dotenv
import app.common.constants as C
from app.common.enums import Environment


class EnvLoggingFilter(logging.Filter):
    def filter(self, record):
        record.env_mark = "<" + str.lower(os.getenv(C.ENV_APP_ENV)) + "-" + C.PROJECT_NAME+ ">"
        return True


def setup_logging(name: str = C.DEFAULT_LOGGER) -> logging.getLogger():
    logger = logging.getLogger(name)
    if len(logger.handlers) < 1:
        log_file_format = "[%(levelname)s] - %(asctime)s - %(name)s - : %(env_mark)s %(message)s in %(pathname)s:%(lineno)d"
        env: Environment = Environment(str.lower(os.getenv(C.ENV_APP_ENV)))
        if env == Environment.Local:
            logger.setLevel(logging.DEBUG)
        elif env == Environment.Development or env == Environment.DevelopmentOut:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(Formatter(log_file_format))
        logger.addHandler(console_handler)
        logger.addFilter(EnvLoggingFilter())
    return logger


def setup_environment(common_env_file_path: str, specific_env_file: str = None):
    load_dotenv(dotenv_path=common_env_file_path)
    if os.getenv(C.ENV_APP_ENV) is None:
        raise ValueError("Unknown environment")
    env: Environment = Environment(str.lower(os.getenv(C.ENV_APP_ENV)))
    if env == Environment.Local:
        alternative_environment: str = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                    "env_files/.env_local")
    elif env == Environment.Development:
        alternative_environment: str = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                    "env_files/.env_dev")

    elif env == Environment.Production:
        alternative_environment: str = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                    "env_files/.env_prod")

    elif env == Environment.Beta:
        alternative_environment: str = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                    "env_files/.env_beta")

    elif env is None:
        alternative_environment: str = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                    "env_files/.env_local")
    else:
        raise ValueError("Unknown environment")
    logging.getLogger(C.DEFAULT_LOGGER).info("Loading {}".format(env.value))
    load_dotenv(dotenv_path=alternative_environment if specific_env_file is None else specific_env_file)
