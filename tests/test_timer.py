import pytest
from unittest.mock import patch, call
from src.timer.timer import timer
import time
import random

@patch('time.sleep', return_value=None)
def test_timer_normal_mode(mock_sleep):
    with patch('random.random', return_value=0.5): 
        timer(5)
        assert mock_sleep.call_count == 5
        assert mock_sleep.call_args_list == [call(1)] * 5

@patch('time.sleep', return_value=None)
@patch('random.choices', return_value=['three_sec_jump'])
def test_timer_three_sec_jump(mock_choices, mock_sleep):
    with patch('random.random', return_value=0.8):  
        timer(5)
        assert mock_sleep.call_count == 5
        assert call(3) in mock_sleep.call_args_list

@patch('time.sleep', return_value=None)
@patch('random.choices', return_value=['three_jumps_per_sec'])
def test_timer_three_jumps_per_sec(mock_choices, mock_sleep):
    with patch('random.random', return_value=0.8): 
        timer(5)
        assert call(0.33) in mock_sleep.call_args_list

@patch('time.sleep', return_value=None)
@patch('random.choices', return_value=['early_stop'])
def test_timer_early_stop(mock_choices, mock_sleep):
    with patch('random.random', return_value=0.8): 
        timer(5)
        assert mock_sleep.call_count == 0

