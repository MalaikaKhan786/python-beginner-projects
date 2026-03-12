import string

alphabet = string.ascii_lowercase

def caesar(text, shift, encrypt=True):
    if not encrypt:
        shift = -shift

    shifted = alphabet[shift:] + alphabet[:shift]

    table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted + shifted.upper()
    )

    return text.translate(table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, False)


encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(encrypted_text, 13)

print(decrypted_text)
