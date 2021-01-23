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
    for i in range(len(plaintext)):
        x = plaintext[i]
        y = keyword[i % len(keyword)]
        if ("a" <= x <= "z"):
            key = (ord(x) + ord(y)) - ord("a")
            if (key > ord("z")):
                key -= 26
        else:
            key = (ord(x) + ord(y)) - ord("A")
            if (key > ord("Z")):
                key -= 26
        ciphertext += chr(key)
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
    for i in range(len(ciphertext)):
        x = ciphertext[i]
        y = keyword[i % len(keyword)]
        if ("a" <= x <= "z"):
            key = (ord(x) - ord(y)) + ord("a")
            if (key < ord("a")):
                key += 26
        else:
            key = (ord(x) - ord(y)) + ord("A")
            if (key < ord("A")):
                key += 26
        plaintext += chr(key)
    return plaintext
