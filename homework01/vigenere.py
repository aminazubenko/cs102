def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    first_small = ord("a")
    last_small = ord("z")
    first_big = ord("A")
    last_big = ord("Z")
    number = 26
    for i, letter in enumerate(plaintext):
        shift = ord((keyword[i % len(keyword)]).lower()) - first_small
        if letter.isalpha() and shift != 0:
            chr_i = ord(letter)
            if first_small <= chr_i <= last_small:
                chr_i += shift
                if chr_i > last_small:
                    chr_i -= number
                ciphertext += chr(chr_i)
            elif first_big <= chr_i <= last_big:
                chr_i += shift
                if chr_i > last_big:
                    chr_i -= number
                ciphertext += chr(chr_i)
        else:
            ciphertext += letter
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    first_small = ord("a")
    last_small = ord("z")
    first_big = ord("A")
    last_big = ord("Z")
    number = 26
    for i, letter in enumerate(ciphertext):
        shift = ord((keyword[i % len(keyword)]).lower()) - first_small
        if letter.isalpha() and shift != 0:
            chr_i = ord(letter)
            if first_small <= chr_i <= last_small:
                chr_i -= shift
                if chr_i < first_small:
                    chr_i += number
                plaintext += chr(chr_i)
            elif first_big <= chr_i <= last_big:
                chr_i -= shift
                if chr_i < first_big:
                    chr_i += number
                plaintext += chr(chr_i)
        else:
            plaintext += letter
    return plaintext
