"""
File for storing decorators of functions used for example for retry logic on database classes
"""
import logging
import time
from functools import wraps
from typing import Callable


def retry_decorator(logger: logging.Logger, attempts: int = 5) -> Callable:
    def inner_decorator(func) -> Callable:
        @wraps(func)
        def modified_func(*args, **kwargs) -> Callable:
            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                except:
                    if attempt == attempts - 1:
                        logger.info("Operation failed during last attempt - raising exception.")
                        raise
                    logger.exception("Retrying operation - attempt {}".format(attempt + 1))
                    time.sleep(min(10, 2 ** attempt))

        return modified_func
    return inner_decorator
