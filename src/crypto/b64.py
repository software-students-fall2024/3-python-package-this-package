def base64(string, type="encode"):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    type =  type.lower()
    
    if type == "encode":
        if string == "": return ""
        binary_str = ''.join([format(ord(char), '08b') for char in string])
        
        padding_length = 6 - len(binary_str) % 6
        binary_str = binary_str + '0' * padding_length
        
        six_bit_chunks = [binary_str[i:i+6] for i in range(0, len(binary_str), 6)]
        
        base64_encoded = ''.join(base64_chars[int(chunk, 2)] for chunk in six_bit_chunks)
        
        padding = "=" * (4 - len(base64_encoded) % 4)

        return base64_encoded + padding
    elif type == "decode":
        if not all(char in base64_chars or char == '=' for char in string): 
            print("Invalid format: Only base64 Characters are allowed(A-Z, a-z, 0-9, +, /, =)")
            return None
        
        string = string.rstrip("=")
        
        binary_str = ''.join([format(base64_chars.index(char), '06b') for char in string])
        
        byte_chunk = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
        
        decoded_str = ''.join([chr(int(byte, 2)) for byte in byte_chunk if len(byte) == 8])
        
        return decoded_str
    else:
        print("Invalid action type: Please select 'encode' or 'decode'.") 
        return None
        
        
    
# string = "="
# encoded = base64(string, "encode")
# print(encoded)
# print(base64(encoded, "decode"))
        