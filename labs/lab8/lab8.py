from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
import hashlib
import random
# a. Return the hexadecimal SHA-256 hash of a
# randomly generated integer converted to a string
def generateTxid():
    number = random.randint(1, 10)

    # return hashlib.sha256(str(number).encode("utf-8")).hexdigest()
    return hex(number)
    
# Function generateInput():
# a. prevTxid = generateTxid()
# b.prevOutputIndex = randomly generate an integer
# between 0 and 5
# c. Return prevTxid, prevOutputIndex

def generateInput():
    prevTxid = generateTxid()
    prevOutputIndex = random.randint(0, 5)

    return prevTxid, prevOutputIndex

# Function generateOutput():
# a.recipientAddress = 'recipient_address_' +
# randomly generate an integer between 1 and 100
# converted to a string
# b. amount = round a random floating-point number
# between 0.001 and 1.0 to 8 decimal places
# c. Return recipientAddress, amount

def generateOutput():
    number = random.randint(1, 100)
    recipientAddress = 'recipient_address_' + str(number)
    amount = round(random.uniform(0.001, 1.0), 8)

    return recipientAddress, amount

# Function generateTransactionFee():
# a. Return round a random floating-point number
# between 0.0001 and 0.001 to 8 decimal places

def generateTransactionFee():
    roundNumber = round(random.uniform(0.0001, 0.001), 8)

    return roundNumber

# Function generateRandomTransaction():
# a. txid = generateTxid()
# b.inputPrevTxid, inputPrevOutputIndex =
# generateInput()
# c. outputRecipientAddress, outputAmount =
# generateOutput()
# d.transactionFee = generateTransactionFee()
# e. Return txid, inputPrevTxid, inputPrevOutputIndex,
# outputRecipientAddress, outputAmount,
# transactionFee

def generateRandomTransaction():
    txid = generateTxid()
    inputPrevTxid = generateInput()
    inputPrevOutputIndex = generateInput()
    outputRecipientAddress = generateOutput()
    outputAmount = generateOutput()
    transactionFee = generateTransactionFee()

    return txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee
    # return hashlib.sha256(str(txid).encode("utf-8")).hexdigest(), hashlib.sha256(str(inputPrevTxid).encode("utf-8")).hexdigest(),hashlib.sha256(str(inputPrevOutputIndex).encode("utf-8")).hexdigest(),  hashlib.sha256(str(outputRecipientAddress).encode("utf-8")).hexdigest(), hashlib.sha256(str(outputAmount).encode("utf-8")).hexdigest(), hashlib.sha256(str(transactionFee).encode("utf-8")).hexdigest()
# Function concatenateString(txid, inputPrevTxid,
# inputPrevOutputIndex, outputRecipientAddress,
# outputAmount, transactionFee):
# a. transactionData = concatenate the values of txid,
# inputPrevTxid, inputPrevOutputIndex,
# outputRecipientAddress, outputAmount, and
# transactionFee into a single string.
# b.Convert non-string values to string data type by
# using str() function.
# c. Return transactionData

def concatenateString(txid, inputPrevTxid,
                      inputPrevOutputIndex, outputRecipientAddress,
                      outputAmount, transactionFee):
    transactionData = txid + str(inputPrevTxid) + str(inputPrevOutputIndex) + str(outputRecipientAddress) + str(outputAmount) + str(transactionFee)

    return transactionData

# Function generateECDSAKeyPair():
# a. ECDSAPrivateKey = generate a private key using
# ec.generate_private_key(ec.SECP256K1())
# b.ECDSAPublicKey = get the corresponding public
# key from ECDSAPrivateKey
# c. Return ECDSAPrivateKey, ECDSAPublicKey

def generateECDSAKeyPair():
    ECDSAPrivateKey = ec.generate_private_key(ec.SECP256K1())
    ECDSAPublicKey = ECDSAPrivateKey.public_key()

    return ECDSAPrivateKey, ECDSAPublicKey

# Function ECDSASign(privateKey, message):
# a.signature = sign the message using
# privateKey.sign(message,
# ec.ECDSA(hashes.SHA256()))
# b.Return signature
def ECDSASign(privateKey, message):
    signature = privateKey.sign(message.encode(), ec.ECDSA(hashes.SHA256()))
    return signature

# Function ECDSAVerify(publicKey, message,
# signature):
# a. Try:
# Verify the signature using
# publicKey.verify(signature, message,
# ec.ECDSA(hashes.SHA256()))
# Return True
# b.Catch any exception:
#  Return False

def ECDSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(signature, message.encode(), ec.ECDSA(hashes.SHA256()))
        return True
    except:
        return False
    
def main():
    txid, inputPrevTxid, inputPrevOutputIndex,outputRecipientAddress, outputAmount, transactionFee = generateRandomTransaction()
    transactionDataAsMessage = concatenateString(txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee).encode()
    # transactionDataAsMessageSHA256Hashed = hashlib.sha256(str(transactionDataAsMessage).encode()).hexdigest()
    transactionDataAsMessageSHA256Hashed = hashlib.sha256(transactionDataAsMessage).hexdigest()
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()
    signature = ECDSASign(ECDSAPrivateKey,transactionDataAsMessageSHA256Hashed)
    verified = ECDSAVerify(ECDSAPublicKey,transactionDataAsMessageSHA256Hashed,signature)
    print( "ECDSA:")
    print( "ECDSA Public Key:", ECDSAPublicKey)
    print( "ECDSA Private Key:", ECDSAPrivateKey)
    print("transactionDataAsMessageSHA256Hashed:",transactionDataAsMessageSHA256Hashed) 
    print( "Signature:", signature)
    print( "Verification:", verified)

main()