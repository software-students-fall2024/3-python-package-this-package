import random
from shutdown.shutdown import shutdown_system
from crypto.b64 import base64
from crypto.morse import morse
from crypto.utils import isMorse, isBase64, randomGibberish
from date.date import get_date_with_error
from calculator.calculator import correct_calculator, wrong_calculator, parse_eq
from timer.timer import timer

def encode(str, type):
    if random.random() <= 0.05:
        shutdown_system()
        
    type = type.lower()
    encodedStr = ""
    
    if random.random() >= 0.7:
        if type == "morse":
            encodedStr = morse(str)
        elif type == "base64":
            encodedStr = base64(str)
        else:
            print("Invalid encoder: Please select from [morse, base64, caesar, vigenere]") 
            return None
    else:
        encoded_chArr = []
        for char in str:
            choice = random.choice(["morse", "base64"])
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
        encodedStr = ''.join(encoded_chArr) 
    return encodedStr 

def decode(str, type):
    if random.random() <= 0.05:
        shutdown_system()
    
    type = type.lower()
    decodedStr = ""
    # Set a probability for normal decoding vs. random decoding
    if random.random() >= 0.7:
        # Normal decoding with 30% probability
        if type == "morse":
            decodedStr = morse(str, "decode")
        elif type == "base64":
            decodedStr = base64(str, "decode")
        else:
            print("Invalid decoder: Please select from [morse, base64, caesar, vigenere]") 
            return None
    else:
        decodedSegments = []
        
        i = 0
        while i < len(str):
            
            segmentLength = random.randint(1, 5)
            segmentEnd = i + segmentLength
            if segmentEnd <= len(str): 
                segment = str[i:segmentEnd]
            else: 
                segment = str[i: len(str)]
                segmentLength = len(str) - i
            
            i += segmentLength

            if random.random() >= 0.5:
                if isMorse(segment):
                    decodedSegments.append(morse(segment, "decode"))
                elif isBase64(segment):
                    decodedSegments.append(base64(segment, "decode"))
                else:
                    decodedSegments.append(randomGibberish(segmentLength))
            else:
                decodedSegments.append(randomGibberish(segmentLength))
        
        decodedStr = ''.join(decodedSegments)
        
    return decodedStr


def get_date():
    if random.random() < 0.05:
        shutdown_system()
    get_date_with_error()
    
def calculator(equation):
    if random.random() <= 0.05:
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
    
def startTimer():
    timer()