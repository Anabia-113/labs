import hashlib
# # part(a)
# file = open('hash.txt', 'r')
# content = file.read()
# print("online hash: ", content)

# part(b)
hash_file ='C27783392976304D9EC296C6CF318F4145E780D02B78C679347E93408553A59C'
with open('Lab5-6-2023.pdf', 'rb') as s:
    sha256_hash = hashlib.sha256(s.read()).hexdigest()
    # uppercase_text = "".join(c.upper() if c.isalnum() else c for c in sha256_hash)
    uppercase_text = sha256_hash.upper()
if uppercase_text == hash_file:
    print("the hash Matches")
else:
    print("the hash is different")

# Question 2
with open('message1.bin', 'rb') as random:
    hash = hashlib.sha256(random.read()).hexdigest()
print("avalanche effect: ", hash)


#questio 3
with open('message1.bin', 'rb') as f:
    print("message1 md5 hash: ", hashlib.md5(f.read()).hexdigest())
    print("message1 sha1 hash: ", hashlib.sha1(f.read()).hexdigest())

with open('message2.bin', 'rb') as f:
    print("message2 md5 hash: ", hashlib.md5(f.read()).hexdigest())
    print("message2 sha1 hash: ", hashlib.sha1(f.read()).hexdigest())