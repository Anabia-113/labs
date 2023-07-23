from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
import hashlib
import random

def generateTxid():
    # Generate a random integer
    random_integer = random.randint(1, 1000000)

    # Convert the integer to a string
    integer_string = str(random_integer)

    # Compute the SHA-256 hash of the string
    sha256_hash = hashlib.sha256(integer_string.encode()).hexdigest()

    # Return the hexadecimal hash
    return sha256_hash


def generateInput():
    # Generate previous transaction ID (prevTxid)
    prevTxid = generateTxid()

    # Generate previous output index (prevOutputIndex)
    prevOutputIndex = random.randint(1, 1000000)

    # Return prevTxid and prevOutputIndex
    return prevTxid, prevOutputIndex


def generateOutput():
    # Generate recipient address (recipientAddress)
    recipient_address = 'recipient_address_' + str(random.randint(1, 1000000))

    # Generate amount with 8 decimal places (amount)
    amount = round(random.uniform(0.001, 0.001), 8)

    # Return recipientAddress and amount
    return recipient_address, amount


def generateTransactionFee():
    # Generate transaction fee with 8 decimal places
    transaction_fee = round(random.uniform(0.0001, 0.001), 8)

    # Return the transaction fee
    return transaction_fee


def generateRandomTransaction():
    # Generate transaction ID (txid)
    txid = generateTxid()

    # Generate input previous transaction ID and output index
    inputPrevTxid, inputPrevOutputIndex = generateInput()

    # Generate output recipient address and amount
    outputRecipientAddress, outputAmount = generateOutput()

    # Generate transaction fee
    transactionFee = generateTransactionFee()

    # Return the generated values
    return txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee


def concatenateString(txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee):
    # Concatenate the values into a single string
    transactionData = str(txid) + str(inputPrevTxid) + str(inputPrevOutputIndex) + str(outputRecipientAddress) + str(outputAmount) + str(transactionFee)
    
    # Return the concatenated string
    return transactionData

def generateECDSAKeyPair():
    private_key = ec.generate_private_key(
        ec.SECP256K1(), default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def ECDSASign(privateKey, message):
    signature = privateKey.sign(
        message.encode(),
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def ECDSAVerify(publicKey, message, signature):
    try:
        publicKey.verify(
            signature,
            message.encode(),
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except:
        return False
    



def main():
    # Generate a random transaction
    txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee = generateRandomTransaction()

    # Concatenate and hash the transaction data
    transactionData = concatenateString(txid, inputPrevTxid, inputPrevOutputIndex, outputRecipientAddress, outputAmount, transactionFee)
    transactionDataAsMessage = transactionData.encode()
    transactionDataAsMessageSHA256Hashed = hashlib.sha256(transactionDataAsMessage).hexdigest()
    
     # Generate ECDSA key pair
    ECDSAPrivateKey, ECDSAPublicKey = generateECDSAKeyPair()
    
    # Sign the transaction data hash
    signature = ECDSASign(ECDSAPrivateKey, transactionDataAsMessageSHA256Hashed)
    
    # Verify the signature
    verified = ECDSAVerify(ECDSAPublicKey, transactionDataAsMessageSHA256Hashed, signature)
    
    # print
    print ("ECDSA:")
    print("ECDSA Public Key:", ECDSAPublicKey)
    print("ECDSA Private Key:", ECDSAPrivateKey)
    print("transactionDataAsMessageSHA256Hashed:", transactionDataAsMessageSHA256Hashed)
    print("Signature:", signature)
    print("Verification:", verified)
    
# Call the main function
main() 
    
    
    

   
    
    
    
        
        
        
        

