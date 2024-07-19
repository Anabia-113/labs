from cryptography.hazmat.primitives.asymmetric import rsa, dsa 
from cryptography.hazmat.primitives import serialization, hashes 
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15 
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
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
# Function generateECDSAKeyPair():
# 1. Generate a private key using ec.generate_private_key()
# function with ec.SECP256K1() as the parameter. Save the
# result in privateKey.
# 2. Obtain the corresponding public key by calling
# privateKey.public_key(). Save the result in publicKey.
# 3. Return privateKey and publicKey.


def generateECDSAKeyPair():
    privateKey = ec.generate_private_key(ec.SECP256K1)
    publicKey = privateKey.public_key()
    return privateKey, publicKey

# Function ECDSASign(privateKey, message):
# 1. Generate a signature by calling privateKey.sign() function
# with message and ec.ECDSA(hashes.SHA256()) as
# parameters. Save the result in signature.
# 2. Return signature.

def ECDSASign(privateKey, message):
    signature = privateKey.sign(
        message, ec.ECDSA(hashes.SHA256())
    )
    return signature

# Function ECDSAVerify(publicKey, message, signature):
# 1. Try the following block of code:
# a. Call publicKey.verify() function with signature, message,
# and ec.ECDSA(hashes.SHA256()) as parameters.
# b. If the verification is successful, return True.
# 2. If any exception occurs (doesn’t verify), return False

def ECDSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(
        signature,
        message,
        ec.ECDSA(hashes.SHA256())
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
    print("signature : ", DSASign(DSAPrivateKey, message))
    sig = DSASign(DSAPrivateKey, message)
    print("\n")
    verified = DSAVerify(DSAPublicKey, message, sig)
    print("Verified: ", verified)

    # Call generateECDSAKeyPair() function. Save the private key
    # in ECDSAPrivateKey and the public key in
    # ECDSAPublicKey.
    print("--------------------ECDSA -------------------")
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()

    # 2. Convert the message e.g. "Message for ECDSA algorithm"
    # to bytes and store it in a message.
    message = b"Message for ECDSA algorithm\n"

    # 3. Call ECDSASign() function with ECDSAPrivateKey and
    # message as parameters. Save the result in signature.
    signature = ECDSASign(ECDSAPrivateKey, message)

    # 4. Call ECDSAVerify() function with ECDSAPublicKey,
    # message, and signature as parameters. Save the result in
    # verified.
    verified = ECDSAVerify(ECDSAPublicKey, message, signature)
    # 5. Print "ECDSA:"
    print("*****************ECDSA***************" )

    # 6. Print "ECDSA Public Key:" followed by the value of
    # ECDSAPublicKey.
    print("ECDSA Public Key:", ECDSAPublicKey, "\n")

    # 7. Print "ECDSA Private Key:" followed by the value of
    # ECDSAPrivateKey.
    print("Ecdsa Private key:", ECDSAPrivateKey)

    # 8. Print "Message:" followed by the decoded value of message.
    print("Message: ", message.decode())
    # 9. Print "Signature:" followed by the value of signature.
    print("signature: ", signature)
    # 10. Print "Verification:" followed by the value of verified.
    print("verification: " , verified)
main()


