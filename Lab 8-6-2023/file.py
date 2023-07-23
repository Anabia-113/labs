from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives import padding


def generateRSAKeyPair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def RSAEncrypt(publicKey, plainText):
    cipherText = publicKey.encrypt(
        plainText,
        PKCS1v15()
    )
    return cipherText

def RSADecrypt(privateKey, cipherText):
    plainText = privateKey.decrypt(
        cipherText,
        PKCS1v15()
    )
    return plainText

def generateDSAKeyPair():
    private_key = dsa.generate_private_key(
        key_size=1024
    )
    public_key = private_key.public_key()
    return private_key, public_key

def DSASign(privateKey, message):
    signature = privateKey.sign(
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

def main():
    # Generate RSA key pair
    RSAprivateKey, RSApublicKey = generateRSAKeyPair()

    # Convert plainText to bytes
    plainText = b"Message for RSA algorithm"

    # Encrypt plainText using RSApublicKey
    cipherText = RSAEncrypt(RSApublicKey, plainText)

    # Decrypt cipherText using RSAPrivateKey
    decryptedText = RSADecrypt(RSAprivateKey, cipherText)

    # Print RSA details
    print("RSA Details:")
    print("RSA Public Key:", RSApublicKey)
    print("RSA Private Key:", RSAprivateKey)
    print("Plaintext:", plainText.decode())
    print("Ciphertext:", cipherText)
    print("Decrypted Text:", decryptedText.decode())

    # Generate DSA key pair
    DSAPrivateKey, DSAPublicKey = generateDSAKeyPair()

    # Convert message to bytes
    message = b"Message for DSA algorithm"

    # Generate signature using DSAPrivateKey
    signature = DSASign(DSAPrivateKey, message)

    # Verify signature using DSAPublicKey
    verified = DSAVerify(DSAPublicKey, message, signature)

    # Print DSA details
    print("\nDSA Details:")
    print("DSA Public Key:", DSAPublicKey)
    print("DSA Private Key:", DSAPrivateKey)
    print("Message:", message.decode())
    print("Signature:", signature)
    print("Verification:", verified)

# Call the main function
main()






# import hashlib

# def calculate_hash(sender, recipient, subject, message, nonce):
#     attempts = 0
#     data = sender + recipient + subject + message + str(nonce)

#     while True:
#         attempts += 1
#         hash_value = hashlib.sha256(data.encode()).hexdigest()

#         if hash_value[:2] == "ff":
#             return hash_value, attempts

#         nonce += 1
#         data = sender + recipient + subject + message + str(nonce)

# # Example usage:
# sender_email = input("Enter sender's email address: ")
# recipient_email = input("Enter recipient's email address: ")
# subject = input("Enter email subject: ")
# message = input("Enter message body: ")
# nonce = int(input("Enter nonce: "))

# hash_value, attempts = calculate_hash(sender_email, recipient_email, subject, message, nonce)

# print("Hash value:", hash_value)
# print("Attempts:", attempts) 






# import hashlib

# def calculate_hash(sender, recipient, subject, message, nonce, difficulty):
#     attempts = 0
#     data = sender + recipient + subject + message + str(nonce)

#     while True:
#         attempts += 1
#         hash_value = hashlib.sha256(data.encode()).hexdigest()

#         if hash_value[:difficulty] == "f" * difficulty:
#             return hash_value, attempts

#         nonce += 1
#         data = sender + recipient + subject + message + str(nonce)

# # Example usage:
# sender_email = input("Enter sender's email address: ")
# recipient_email = input("Enter recipient's email address: ")
# subject = input("Enter email subject: ")
# message = input("Enter message body: ")
# nonce = int(input("Enter nonce: "))

# difficulty_level_1 = 2
# difficulty_level_2 = 4

# hash_value_1, attempts_1 = calculate_hash(sender_email, recipient_email, subject, message, nonce, difficulty_level_1)
# hash_value_2, attempts_2 = calculate_hash(sender_email, recipient_email, subject, message, nonce, difficulty_level_2)

# print("Difficulty Level 1:")
# print("Hash value:", hash_value_1)
# print("Attempts:", attempts_1)

# print("\nDifficulty Level 2:")
# print("Hash value:", hash_value_2)
# print("Attempts:", attempts_2)