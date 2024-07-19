import hashlib as hb
import bcrypt as b

#bcrypt
data = b"murtaza"
salt = b.gensalt()
hashed_text = b.hashpw(data, salt)
print("bcrypt1: ",hashed_text)

data = "murtazak"

#md5
print("md5: " + hb.md5(data.encode()).hexdigest())


#SHA-1
hash_object = hb.sha1(data.encode()).hexdigest()
print("sha1: ", hash_object)

#SHA-256
hash_object = hb.sha3_256(data.encode()).hexdigest()
print("SHA-256: ", hash_object)

#SHA512
hash_object = hb.sha512(data.encode()).hexdigest()
print("SHA512: ", hash_object)

#SHA-3
hash_object = hb.sha3_384(data.encode()).hexdigest()
print("Sha3: ", hash_object)

#BLAKE2
hash_object = hb.blake2b(data.encode()).hexdigest()
print("BLAKE2 ", hash_object)

#RIPEMD-160
hash_object = hb.new('ripemd160', data.encode()).hexdigest()
print("RIPEMD-160:", hash_object)
