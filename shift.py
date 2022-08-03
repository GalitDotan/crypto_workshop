from cesar_enc import *


# result = incryptographyacaesarcipheralsoknownastheshiftciphercaesarscodeorcaesarshiftisoneofthesimplestandmostwidelyknownencryptiontechniquesitisatypeofsubstitutioncipherinwhicheachletterintheplaintextisreplacedbyalettersomefixednumberofpositionsdownthealphabetforexamplewithaleftshiftofsdwouldbereplacedbyaewouldbecomebandsoonthemethodisnamedafterjuliuscaesarwhouseditinhisprivatecorrespondenced

def decipher_shift(data):
    for i in range(1, 25):
        res = shift_enc(data, i)
        if res.startswith("incrypto"):
            print(res)
            print("i =", i)


if __name__ == '__main__':
    with open("ciphertext.txt") as f:
        data = f.read()
        decipher_shift(data.lower())
