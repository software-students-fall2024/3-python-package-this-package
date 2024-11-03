import pytest
from morse import morse
from b64 import base64

#Morse Tests
valid_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789"
morse_encoded = (
    ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..   ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----."
)

@pytest.mark.parametrize("inp, expected", [(valid_char, morse_encoded), ("", "")])
def test_morse_encode(inp, expected):
    actual = morse(inp, "encode")
    assert actual == expected, f"1. Expected encoding morse() to return \n{expected}. Instead, it returned \n{actual}."

@pytest.mark.parametrize("inp, expected", [(morse_encoded, valid_char), ("", "")])
def test_morse_decode(inp, expected):
    actual = morse(inp, "decode")
    assert actual == expected, f"2. Expected decoding morse() to return \n{expected}. Instead, it returned \n{actual}."
    
def test_morse_invalid_characters_encode():
    assert morse("!", "encode") is None, f"3. Expected encoding morse() with invalid chars to return None."
    
def test_morse_invalid_characters_decode():
    assert morse("A", "decode") is None, f"4. Expected decoding morse() with invalid chars to return None."
    
def test_morse_invalid_type():
    assert morse("HELLO", "translate") is None, f"5. Expected morse() with invalid type to return None."
    
#Base64 Tests
@pytest.mark.parametrize("inp, expected", [("base64+=./", "YmFzZTY0Kz0uLw=="), ("", "")])
def test_b64_encode(inp, expected):
    actual = base64(inp, "encode")
    assert actual == expected, f"6. Expected encoding base64() to return \n{expected}. Instead, it returned \n{actual}."
    
@pytest.mark.parametrize("inp, expected", [("aGVsbG8=", "hello"), ("TU9SU0U=", "MORSE"), ("dGVzdA==", "test"), ("", "")])
def test_b64_decode(inp, expected):
    actual = base64(inp, "decode")
    assert actual == expected, f"7. Expected decoding base64() to return \n{expected}. Instead, it returned \n{actual}."
    
def test_b64_invalid_characters():
    assert base64("!", "decode") is None, f"8. Expected decoding base64() with invalid chars to return None."
    
def test_b64_invalid_type():
    assert base64("Hello", "translate") is None, f"9. Expected base64() with invalid type to return None."
    


    
