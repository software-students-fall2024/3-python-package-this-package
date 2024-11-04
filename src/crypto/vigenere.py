def vigenere(string, keyword="key", type="encode"):
    '''
    If input string contains non-letter characters, each such character will be skipped while the index into 
    the keyword will still be incremented (moved to the next character in the keyword).
    '''
    result = ""  # encoding or decoding result
    if (not isinstance(keyword, str)) or ((not keyword.isalpha()) and (not keyword == "")):
        print("Invalid keyword: Only strings of English letters (A-Z, a-z) are allowed.")
        return None
    
    keyword_len = len(keyword)
    if not keyword_len:
        # if keyword is empty string
        return string
    
    if type == "encode":
        i = 0
        for char in string:
            if char.isalpha():
                if char.isupper():
                    result += chr(ord("A") + (ord(char) + ord(keyword[i].upper()) - 2 * ord("A")) % 26)
                else:
                    result += chr(ord("a") + (ord(char) + ord(keyword[i].lower()) - 2 * ord("a")) % 26)
            else:
                result += char
            i = (i + 1) % keyword_len
    elif type == "decode":
        i = 0
        for char in string:
            if char.isalpha():
                if char.isupper():
                    result += chr(ord("A") + (ord(char) - ord(keyword[i].upper())) % 26)
                else:
                    result += chr(ord("a") + (ord(char) - ord(keyword[i].lower())) % 26)
            else:
                result += char
            i = (i + 1) % keyword_len
    else:
        print("Invalid action type: Please select 'encode' or 'decode'.") 
        return None
    
    return result