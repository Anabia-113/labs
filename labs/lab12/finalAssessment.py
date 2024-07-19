import hashlib

def cal(senderEmail, recipientEmail, emailSubject, messageBody, nonce):
    combo = str(senderEmail) + str(recipientEmail) + str(emailSubject) + str(messageBody) + str(nonce)
    hash = hashlib.sha256(combo.encode()).hexdigest()
    return hash

senderEmail = "gmkh@gmail.com",
recipientEmail = "umairjavaidmanj@gmail.com",
emailSubject = "proof of work",
messageBody ="sdfsd",
nonce = 0

print("first two hexadecimal digits")
for i in range(0,9999):
    nonce = i
    hashed = cal(senderEmail,recipientEmail, emailSubject, messageBody, nonce)
    if(hashed[:2] == "ff"):
        print(hashed)
        print("attempts: ", nonce)
        break
print("")

print("first four hexadecimal digits")
for i in range(0,999999):
    nonce = i
    hashed = cal(senderEmail,recipientEmail, emailSubject, messageBody, nonce)
    if(hashed[:4] == "ffff"):
        print(hashed)
        print("attempts: ", nonce)
        break

# while nonce < 9999:
#     hashed = cal(senderEmail,recipientEmail, emailSubject, messageBody, nonce)
#     if(hashed[:2] == "ff"):
#         print(hashed)
#         break
#     nonce += 1

# while nonce < 999999:
#     hashed = cal(senderEmail,recipientEmail, emailSubject, messageBody, nonce)
#     if(hashed[:4] == "ffff"):
#         print(hashed)
#         break
#     nonce += 1