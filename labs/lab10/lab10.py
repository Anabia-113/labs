import hashlib
import base58
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# b. Write a function that generates and returns the 
# ECDSA public and private keys. 
# c. Write a function that takes the ECDSA public key as 
# input parameter and returns a bitcoin wallet address. 
# You can follow the steps shown in figure 1. 
# [Note: To pass the public key as bytes you can use the 
# public_bytes method from cryptography library. 
# publicKeyBytes = publicKey.public_bytes(
#  encoding=serialization.Encoding.X962,
#  format=serialization.PublicFormat.UncompressedPoint
# )]


def generateECDSA():
    ECDSAPrivateKey = ec.generate_private_key(ec.SECP256K1())
    ECDSAPublicKey = ECDSAPrivateKey.public_key()
    return ECDSAPrivateKey, ECDSAPublicKey


def bitcoinWalletAddress(ECDSAPublicKey):

    # generating sha256 hash
    sha256hash = hashlib.sha256(ECDSAPublicKey).hexdigest()
    
    # generating ripemd160 hash
    Ripemd160Hash = hashlib.new('ripemd160', sha256hash.encode()).digest()

    net_ripemd_hash = b'00' + Ripemd160Hash

    shaHashOfRipemd160 = hashlib.sha256(Ripemd160Hash).hexdigest()
    version_shaHashOfRipemd160 = hashlib.sha256(shaHashOfRipemd160.encode()).hexdigest()
    
    checksum = version_shaHashOfRipemd160[:4]
    base = checksum + version_shaHashOfRipemd160
    address = base58.b58encode(base)

    print("sha:", sha256hash)
    print("ripe:", Ripemd160Hash)
    print("sha2256 of ripe:", shaHashOfRipemd160)
    print("version_shahash of ripe:", version_shaHashOfRipemd160)
    print("address:", address.decode())
    

    return address


ECDSAPrivateKey, ECDSAPublicKey = generateECDSA()
publicKeyBytes = ECDSAPublicKey.public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint)
bitcoinWalletAddress(publicKeyBytes)
