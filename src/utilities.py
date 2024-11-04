import random
import string
from shutdown.shutdown import shutdown_system
from crypto.b64 import base64
from crypto.morse import morse
from crypto.caesar import caesar
from crypto.vigenere import vigenere
from crypto.utils import is_morse, is_base64, random_gibberish
from date.date import get_date_with_error
from calculator.calculator import correct_calculator, wrong_calculator, parse_eq
from timer.timer import timer


def encode(inp_str, type, shift=1, keyword="key"):
    if random.random() <= 0.01:
        shutdown_system()
    
    type = type.lower()
    enc_str = ""
    
    prob = random.random()
    if prob >= 0.5:
        if type == "morse":
            enc_str = morse(inp_str)
        elif type == "base64":
            enc_str = base64(inp_str)
        elif type == "caesar":
            enc_str = caesar(inp_str, shift)
        elif type == "vigenere":
            enc_str = vigenere(inp_str, keyword)
        else:
            print("Invalid encoder: Please select from [morse, base64, caesar, vigenere]") 
            return None
    else:
        encoded_chArr = []
        for char in inp_str:
            choice = random.choice(["morse", "base64", "caesar", "vigenere"])
            if not(char.isalnum() or char.isspace()):
                if random.random() >= 0.5:
                    choice = "base64"
                else:
                    encoded_chArr.append(char)
                    continue      
            if choice == "morse":
                encoded_chArr.append(morse(char))
            elif choice == "base64":
                encoded_chArr.append(base64(char))
            elif choice == "caesar":
                rand_shift = random.randint(1, 26)  # choose a random shift
                encoded_chArr.append(caesar(char, rand_shift))
            elif choice == "vigenere":
                encoded_chArr.append(vigenere(char, random.choice(string.ascii_letters)))  # use random letter as keyword
        enc_str = ''.join(encoded_chArr) 
    return enc_str 

def decode(inp_str, type, shift=1, keyword="key"):
    if random.random() <= 0.01:
        shutdown_system()
    
    type = type.lower()
    dec_str = ""
    # Set a probability for normal decoding vs. random decoding
    prob = random.random()  # can check with print(prob)
    if prob >= 0.5:
        # Normal decoding with 50% probability
        if type == "morse":
            dec_str = morse(inp_str, "decode")
        elif type == "base64":
            dec_str = base64(inp_str, "decode")
        elif type == "caesar":
            dec_str = caesar(inp_str, shift, "decode")
        elif type == "vigenere":
            dec_str = vigenere(inp_str, keyword, "decode")
        else:
            print("Invalid decoder: Please select from [morse, base64, caesar, vigenere]") 
            return None
    else:
        decoded_segments = []
        
        i = 0
        while i < len(inp_str):
            segment_length = random.randint(1, 5)
            segment_end = i + segment_length
            if segment_end <= len(inp_str): 
                segment = inp_str[i : segment_end]
            else: 
                segment = inp_str[i : len(inp_str)]
                segment_length = len(inp_str) - i
            
            i += segment_length

            if random.random() >= 0.5:
                choice = random.choice(["morse", "base64", "caesar", "vigenere"])
                if choice == "morse" and is_morse(segment):
                    decoded_segments.append(morse(segment, "decode"))
                elif choice == "base64" and is_base64(segment):
                    decoded_segments.append(base64(segment, "decode"))
                elif choice == "caesar":
                    rand_shift = random.randint(1, 26)  # choose a random shift
                    decoded_segments.append(caesar(segment, rand_shift, "decode"))
                elif choice == "vigenere":
                    decoded_segments.append(vigenere(segment, string.ascii_letters, "decode"))  # use alphabet as keyword
            else:
                decoded_segments.append(random_gibberish(segment_length))
        
        dec_str = ''.join(decoded_segments)
        
    return dec_str


def get_date():
    if random.random() < 0.01:
        shutdown_system()
    return get_date_with_error()
    
def calculator(equation):
    if random.random() <= 0.01:
        shutdown_system()
        
    if not isinstance(equation, str):
        print("Warning: Please pass the equation as a string, like '4 - 8 + 9 / 2'.")
        return
    
    result = parse_eq(equation)
    if isinstance(result, str):
        print(result)
        return
    numbers, operators = result
    probabilities = random.randint(0,1)
    if probabilities > 0.7:
        result = wrong_calculator(numbers[:], operators[:])
    else:
        result = correct_calculator(numbers[:], operators[:])
    print(f"The result is: {result}")
    
def start_timer(time = 20):
    timer(time)