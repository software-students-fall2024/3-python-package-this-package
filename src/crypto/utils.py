#Main Function for Encoders and Decoders
import random
import string

def isMorse(segment):
    return all(c in ".-" or c.isspace() for c in segment)

def isBase64(segment):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    return all(c in base64_chars or c == '=' for c in segment)

def randomGibberish(n):
    return ''.join(random.choice(string.ascii_letters + string.digits + "+/.-= ") for _ in range(n))

