import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if (ord(i) >= ord("a")) and (ord(i) <= ord("z")):
            if (ord(i) + shift) > ord("z"):
                ciphertext += chr((ord(i) + shift) - 26)
            else:
                ciphertext += chr(ord(i) + shift)
        elif (ord(i) >= ord("A")) and (ord(i) <= ord("Z")):
            if (ord(i) + shift) > ord("Z"):
                ciphertext += chr((ord(i) + shift) - 26)
            else:
                ciphertext += chr(ord(i) + shift)
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if (ord(i) >= ord("a")) and (ord(i) <= ord("z")):
            if (ord(i) - shift) < ord("a"):
                plaintext += chr((ord(i) - shift) + 26)
            else:
                plaintext += chr(ord(i) - shift)
        elif (ord(i) >= ord("A")) and (ord(i) <= ord("Z")):
            if (ord(i) - shift) < ord("A"):
                plaintext += chr((ord(i) - shift) + 26)
            else:
                plaintext += chr(ord(i) - shift)
        else:
            plaintext += i
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    for i in dictionary:
        for j in range(1, 26):
            wd = decrypt_caesar(i, j)
            if wd == ciphertext:
                return j
    return best_shift
