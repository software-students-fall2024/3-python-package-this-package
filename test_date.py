import pytest
from datetime import datetime, timedelta
import re
from date import get_date_with_error, generate_correct_format_wrong_date, generate_absurd_date, generate_code_snippet

def test_get_date_with_error():
    datetime_regex = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    result = get_date_with_error()
    
    if result.startswith("right:"):
        date_str = result.split("right: ")[1]
        assert datetime_regex.match(date_str), f"Expected datetime format, got {date_str}"
    elif result.startswith("wrong_case1:"):
        date_str = result.split("wrong_case1: ")[1]
        assert datetime_regex.match(date_str), f"Expected datetime format, got {date_str}"
    elif result.startswith("wrong_case2:"):
        date_str = result.split("wrong_case2:")[1]
        absurd_year = int(date_str.split("-")[0])
        assert absurd_year >= 3000 or absurd_year < 1923, f"Expected absurd year, got {absurd_year}"
    elif result.startswith("code:"):
        code_snippets = [
            "print('Hello, World!')",
            "for i in range(10): print(i)",
            "if x > 10:\n    print('x is large')",
            "def add(a, b): return a + b"
        ]
        code = result.split("code: ")[1]
        assert code in code_snippets, f"Expected code snippet, got {code}"

# Test for generate_correct_format_wrong_date
def test_generate_correct_format_wrong_date():
    datetime_regex = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    result = generate_correct_format_wrong_date()
    assert result.startswith("wrong_case1:")
    date_str = result.split("wrong_case1: ")[1]
    assert datetime_regex.match(date_str), f"Expected datetime format, got {date_str}"

# Test for generate_absurd_date
def test_generate_absurd_date():
    datetime_regex = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    result = generate_absurd_date()
    assert result.startswith("wrong_case2:")
    date_str = result.split("wrong_case2:")[1].strip()
    assert datetime_regex.match(date_str), f"Expected datetime format, got {date_str}"
    absurd_year = int(date_str.split("-")[0])
    assert absurd_year >= 3000, f"Expected absurd year, got {absurd_year}"

# Test for generate_code_snippet
def test_generate_code_snippet():
    result = generate_code_snippet()
    assert result.startswith("code:")
    code_snippets = [
        "print('Hello, World!')",
        "for i in range(10): print(i)",
        "if x > 10:\n    print('x is large')",
        "def add(a, b): return a + b"
    ]
    code = result.split("code: ")[1]
    assert code in code_snippets, f"Expected code snippet, got {code}"

if __name__ == "__main__":
    pytest.main()
