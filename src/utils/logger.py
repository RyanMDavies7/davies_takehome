import logging
import logging.config
import time
import yaml
from functools import wraps

# Load the logging configuration from configs/logging.yaml
with open('configs/logging.yaml', 'r') as f:
    config = yaml.safe_load(f)
    logging.config.dictConfig(config)

# Get the logger
logger = logging.getLogger('my_app_logger')

def log_function_data(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Log the function name and arguments
        logger.debug(f"Calling function: {func.__name__} with args: {args} and kwargs: {kwargs}")

        # Track execution time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        # Log the execution time
        logger.debug(f"Function {func.__name__} executed in {end_time - start_time:.4f} seconds")

        return result

    return wrapper
