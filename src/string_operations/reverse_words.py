from src.utils.logger import log_function_data


@log_function_data
def reverse_string(string: str) -> str:
    return string[::-1]