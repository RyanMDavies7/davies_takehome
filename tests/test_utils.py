import pytest
import logging
import time
from src.utils.logger import log_function_data  # Assuming the decorator is in utils/logging_decorator.py

# Sample function to be decorated
@log_function_data
def sample_function(x, y):
    time.sleep(0.1)  # Simulate some processing
    return x + y

def test_log_function_data_decorator(caplog):
    # Call the decorated function and capture the logs
    with caplog.at_level(logging.DEBUG):  # Set logging level to capture DEBUG logs
        result = sample_function(3, 5)

    # Verify that the function returned the correct result
    assert result == 8

    # Verify that the log messages contain the correct information
    assert "Calling function: sample_function with args: (3, 5)" in caplog.text
    assert "Function sample_function executed in" in caplog.text

    # Optionally, check that specific log entries match what you expect
    logs = [record.message for record in caplog.records]
    assert logs[0].startswith("Calling function: sample_function")
    assert logs[1].startswith("Function sample_function executed in")
