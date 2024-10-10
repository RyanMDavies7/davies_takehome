from src.utils.logger import log_function_data


@log_function_data
def calculate_clock_angle(hour, minute):
    hour_angle = hour * 30 + minute * 0.5
    minute_angle = minute * 6

    ans = abs(hour_angle - minute_angle)

    return min(360 - ans, ans)