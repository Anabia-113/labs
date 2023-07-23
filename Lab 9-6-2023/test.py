from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, dsa
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend


def generateECDSAKeyPair():
    private_key = ec.generate_private_key(
        ec.SECP256K1(), default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def ECDSASign(privateKey, message):
    signature = privateKey.sign(
        message,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

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

def main():
    # Generate ECDSA key pair
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()

    # Convert plainText to bytes
    message = b"Message for ECDSA algorithm"

    # Generate signature using ECDSAPrivateKey
    signature = ECDSASign(ECDSAPrivateKey, message)

    # Verify signature using ECDSAPublicKey
    verified = ECDSAVerify(ECDSAPublicKey, message, signature)
    
    
    print("ECDSA:")
    print("ECDSA Public Key:", ECDSAPublicKey)
    print("ECDSA Private Key:", ECDSAPrivateKey)
    print("Message:", message.decode())
    print("Signature:", signature)
    print("Verification:", verified)

# Call the main function
main()  