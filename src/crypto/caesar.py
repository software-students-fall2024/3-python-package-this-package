def caesar(string, shift=1, type="encode"):
    '''
    For encoder, shift shifts letters to the right.
    For decoder, shift means the shift used when encoding, so
    decoding should shift letters to the left.
    '''
    result = ""  # encoding or decoding result
    if not isinstance(shift, int):
        print("Invalid shift: Only integer values are allowed.")
        return None
    
    if type == "encode":
        for char in string:
            if char.isalpha():
                if char.isupper():
                    result += chr(ord("A") + (ord(char) + shift - ord("A")) % 26)
                else:
                    result += chr(ord("a") + (ord(char) + shift - ord("a")) % 26)
            else:
                result += char
    elif type == "decode":
        for char in string:
            if char.isalpha():
                if char.isupper():
                    result += chr(ord("A") + (ord(char) - shift - ord("A")) % 26)
                else:
                    result += chr(ord("a") + (ord(char) - shift - ord("a")) % 26)
            else:
                result += char
    else:
        print("Invalid action type: Please select 'encode' or 'decode'.") 
        return None
    
    return result