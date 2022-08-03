# result = encryption
alphabet = "abcdefghijklmnopqrstuvwxyz"


def shift_enc(plaintext_string, shift):
    new_message = ""
    for c in plaintext_string:
        index = ord(c) - ord("a")
        new_message += alphabet[(index + shift) % 26]
    return new_message


def shift_dec(ciphertext_string, shift):
    return shift_enc(ciphertext_string, shift * -1)


if __name__ == '__main__':
    message = "hqfubswlrq"
    enc = shift_enc(message, 3)
    dec = shift_dec(message, 3)
    print(enc)
    print(dec)
