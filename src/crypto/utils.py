#Main Function for Encoders and Decoders
import random
import string

def is_morse(segment):
    return all(c in ".-" or c.isspace() for c in segment)

def is_base64(segment):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    return all(c in base64_chars or c == '=' for c in segment)

def random_gibberish(n):
    return ''.join(random.choice(string.ascii_letters + string.digits + "+/.-= ") for _ in range(n))

