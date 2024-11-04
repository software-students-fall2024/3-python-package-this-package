
def morse(string, type="encode"):
    morse_dict = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
        'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
        'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
        'Z': '--..',  '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ' ': ' '
    }
    reverse_morse_dict = {value: key for key, value in morse_dict.items()}
    
    type = type.lower()
    
    if type == "encode":
        if not all(char.isalnum() or char.isspace() for char in string): 
            print("Invalid format: Only alphanumeric characters and spaces are allowed.")
            return None
        morse_code = []
        for char in string.upper():
            if char in morse_dict:
                morse_code.append(morse_dict[char])
        return ' '.join(morse_code)
    elif type == "decode":
        if not all(char.isspace() or char == '.' or char == '-' for char in string): 
            print("Invalid format: Only dots, dashes, and spaces are allowed for decoding")
            return None
        words = string.split('   ')
        decoded_text = []
        
        for word in words:
            decoded_word = []
            for symbol in word.split():
                if symbol in reverse_morse_dict:
                    decoded_word.append(reverse_morse_dict[symbol])
            decoded_text.append(''.join(decoded_word))
        return ' '.join(decoded_text)
    else:
        print("Invalid action type: Please select 'encode' or 'decode'.") 
        return None