import bcrypt
import hashlib

# print ("hello world")

name_id ='Anabia'

hello_name = name_id.encode()

print(hello_name)


# md5 = hashlib.sha512(name_id.encode()).hexdigest()
md51 = hashlib.sha256(name_id.encode()).hexdigest()
# md5 = hashlib.sha512(name_id.encode()).hexdigest()
md52 = hashlib.sha1(name_id.encode()).hexdigest()
md53 = hashlib.sha512(name_id.encode()).hexdigest()
md54 = hashlib.blake2b(name_id.encode()).hexdigest()

print(md51)
print(md52)
print(md54)
print(md53)
# print(md5)o








