from utilities import calculator, encode, decode, get_date, start_timer

equations = [
    "3 + 6 * 8",
    "12 - 4 / 2 + 5",
    "7 * 5 - 3 / 1",
    "3 +",
    "3+6*8",
    "3 - 5 *",
    "+ 5 - 2",
    "4.5 + 3",
    5 + 3,
    "9 / 0 + 4"
]

print("TESTING calculator(equation: str)\n")

for eq in equations:
    print(f"Equation: {eq}")
    calculator(eq)


input_str = "TESTING CODE 101"

encode_codes = [
    {
        "input_str": input_str,
        "type": "caesar",
        "shift": 3
    },
    {
        "input_str": input_str,
        "type": "Vigenere",
        "keyword": "key"
    },
    {
        "input_str": input_str,
        "type": "MORSE"
    },
    {
        "input_str": input_str,
        "type": "base64"
    }
]

print("\nTESTING Encoder(code: str, type: str, shift: int, keyword: str)\n")

for encode_code in encode_codes:
    input_str = encode_code["input_str"]
    enc_type = encode_code["type"]
    shift = encode_code.get("shift", 1) 
    keyword = encode_code.get("keyword", "key")  
    
    print(f"Encoded Result: {encode(input_str, enc_type, shift, keyword)}\n")


decode_codes = [
    {
        "input_str": "input string",
        "type": "caesar",
        "shift": 3
    },
    {
        "input_str": "input String1",
        "type": "Vigenere",
        "keyword": "key"
    },
    {
        "input_str": ".- -..",
        "type": "MORSE"
    },
    {
        "input_str": "aGVsbG8=",
        "type": "base64"
    }
]

print("\nTESTING Decoder(code: str, type: str, shift: int, keyword: str)\n")

for decode_code in decode_codes:
    input_str = decode_code["input_str"]
    dec_type = decode_code["type"]
    shift = decode_code.get("shift", 1) 
    keyword = decode_code.get("keyword", "key")  
    
    print(f"Decoded Result: {decode(input_str, dec_type, shift, keyword)}\n")

print("TESTING get_date()")

print(get_date())

print("TESTING timer()")

start_timer()
start_timer(5)