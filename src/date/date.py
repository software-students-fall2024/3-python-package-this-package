import random
from datetime import datetime, timedelta
from shutdown.shutdown import shutdown_system

def generate_correct_format_wrong_date():
    current_datetime = datetime.now()
    random_days = random.randint(-1000, 1000)
    random_hours = random.randint(-12, 12)
    random_minutes = random.randint(-60, 60)
    absurd_datetime = current_datetime + timedelta(days=random_days, hours=random_hours, minutes=random_minutes)
    return f"wrong_case1: {absurd_datetime.strftime('%Y-%m-%d %H:%M:%S')}"

def generate_absurd_date():
    absurd_datetime = datetime(random.randint(3000, 9999), random.randint(1, 12), random.randint(1, 28),
                               random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
    return f"wrong_case2: {absurd_datetime.strftime('%Y-%m-%d %H:%M:%S')}"

def generate_code_snippet():
    code_snippets = [
        "print('Hello, World!')",
        "for i in range(10): print(i)",
        "if x > 10:\n    print('x is large')",
        "def add(a, b): return a + b"
    ]
    return f"code: {random.choice(code_snippets)}"

def get_date_with_error():
    if random.random() < 0.7:
        error_type = random.choice(["correct_format_wrong_date", "absurd_date", "code_snippet"])
        
        if error_type == "correct_format_wrong_date":
            return generate_correct_format_wrong_date()
        
        elif error_type == "absurd_date":
            return generate_absurd_date()
        
        elif error_type == "code_snippet":
            return generate_code_snippet()
    
    current_datetime = datetime.now()
    return f"right: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}"