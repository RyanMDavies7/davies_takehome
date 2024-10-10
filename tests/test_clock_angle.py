import pytest
from src.clock.clock_angles import calculate_clock_angle

def test_calculate_clock_angle():
    assert calculate_clock_angle(12, 0) == 0
    assert calculate_clock_angle(3, 0) == 90
    assert calculate_clock_angle(6, 0) == 180
    assert calculate_clock_angle(9, 0) == 90
    assert calculate_clock_angle(10, 15) == 142.5
