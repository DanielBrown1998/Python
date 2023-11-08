def cipher(txt):
    encrypted = ''
    for c in str(txt).upper():
        if c.isspace() or not c.isalpha():
            continue
        code = ord(c) + 1
        if code >= ord('Z'):
            code = ord('A')
        char = chr(code)
        encrypted += char

    return encrypted


def decipher(txt):
    original = ''
    for c in str(txt).upper():
        if c.isspace() or not c.isalpha():
            continue
        code = ord(c) - 1
        if code >= ord('Z'):
            code = ord('A')
        char = chr(code)
        original += char
    return original

