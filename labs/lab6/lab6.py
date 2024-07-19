from cryptography.hazmat.primitives.asymmetric import rsa, dsa 
from cryptography.hazmat.primitives import serialization, hashes 
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15 
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
import hashlib
# 1. Generate a private key using
# rsa.generate_private_key() function with
# public_exponent and key_size as parameters. Save the
# result in privateKey.
# a. Set public_exponent to 65537
# b. Set key_size to 2048
# 2. Obtain the corresponding public key by calling
# privateKey.public_key(). Save the result in publicKey.
# 3. Return privateKey and publicKey.

def generateRSAKeyPair(pe, ks):
    privateKey = rsa.generate_private_key(pe, ks)
    publicKey = privateKey.public_key()
    return privateKey, publicKey

# Function RSAEncrypt(publicKey, plainText):
# 1. Encrypt plainText using the encrypt(plainText, padding
# technique) method of publicKey. Use PKCS1v15()
# padding. Save the result in cipherText.
# 2. Return the resulting cipherText


def RSAEncrypt(publicKey, plainText):
    ciphertext = publicKey.encrypt(
        plainText,
        padding.PKCS1v15()
    )

    return ciphertext

def RSADecrypt(privateKey, cipherText):
    plaintext = privateKey.decrypt(
        cipherText,
        padding.PKCS1v15()
    )

    return plaintext

def generateDSAKeyPair(key_size):
     DSAPrivateKey = dsa.generate_private_key(key_size)
     DSAPublicKey = DSAPrivateKey.public_key()
     return DSAPrivateKey, DSAPublicKey

def DSASign(private_key, message):
    signature = private_key.sign(
    message,
    hashes.SHA256()
    )
    return signature

def DSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(
        signature,
        message,
        hashes.SHA256()
)
        return True
    except:
        return False
# Function main():
# 1. Generate an RSA key pair by calling
# generateRSAKeyPair(). Store the returned keys as
# RSAprivateKey and RSApublicKey.
# 2. Convert the message e.g "Message for RSA algorithm"
# to bytes and store it in plainTex
# 3. Encrypt plainText using RSAEncrypt(RSAPublicKey,
# plainText). Store the result in cipherText.
# 4. Decrypt cipherText using RSADecrypt(RSAPrivateKey,
# cipherText) function with privateKey. Store the result in
# decryptedText.
# 5. Print RSA details:
# a. RSA Public Key: RSAPublicKey
# b. RSA Private Key: RSAPrivateKey
# c. Plaintext: Decode plainText
# d. Ciphertext: cipherText
# e. Decrypted Text: decryptedText

def main():
    plainText = b"Message for RSA algorithm"
    public_exponent =65537
    key_size = 2048
    generateRSAKeyPair(public_exponent, key_size)
    prikey, pubkey = generateRSAKeyPair(public_exponent, key_size)
    print("RSA public key: ", pubkey)
    print("\n")
    print("RSA rivate key: ", prikey)
    print("\n")
    print("plaintext: ", plainText)
    print("\n")
    print(RSAEncrypt(pubkey, plainText))
    print("\n")
    ct = RSAEncrypt(pubkey, plainText)
    print("Decripted plaintext: ",RSADecrypt(prikey, ct))
    print("\n")
    print("-------------------------------------------------------")
    
    message = b"Message for DSA algorithm"
    DSAPrivateKey, DSAPublicKey = generateDSAKeyPair(key_size)
    print("DSA public key: ", DSAPublicKey)
    print("\n")
    print("DSA rivate key: ", DSAPrivateKey)
    print("\n")
    print("message: ", message)
    print("\n")
    print("signature: ", DSASign(DSAPrivateKey, message))
    sig = DSASign(DSAPrivateKey, message)
    print("\n")
    verified = DSAVerify(DSAPublicKey, message, sig)
    print("Verified: ", verified)

main()

# 6. Generate a DSA key pair by calling
# generateDSAKeyPair(). Store the returned keys as
# DSAPrivateKey and DSAPublicKey.
# 7. Convert the message e.g "Message for DSA algorithm"
# to bytes and store it in a message.
# 8. Generate a signature by calling the
# DSASign(DSAPrivateKey, message) function with
# privateKey and message as parameters. Store the
# result in signature.
# 9. Verify the signature by calling
# DSAVerify(DSAPublicKey, message, signature) function
# with publicKey, message, and signature as parameters.
# Store the result in verified.
# a. Print DSA details:
# b. DSA Public Key: DSAPublicKey
# c. DSA Private Key: DSAPrivateKey
# d. Message: Decode message
# e. Signature: signature
# f. Verification: verified
# 10. Call the main() function.

