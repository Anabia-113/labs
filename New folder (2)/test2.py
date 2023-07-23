import hashlib
import random
import string
with open('Lab5-6-2023.pdf', 'rb') as file:
    binary_data = file.read()
    online_value='c27783392976304d9ec296c6cf318f4145e780d02b78c679347e93408553a59c'
    def calculate_sha256(data):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data)
        return sha256_hash.hexdigest()

# Example usage
input_data = "Hello, world!"  # Can be a string or binary data
sha256_result = calculate_sha256(binary_data)
print("SHA-256:", sha256_result)
if(sha256_result == online_value):
    print('Is Equal')
else:
    print('not equal')
    
    
    
    
    
    
    
    
def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()

    with open(file_path, 'rb') as file:
        # Read the file in chunks to handle large files efficiently
        for chunk in iter(lambda: file.read(4096), b''):
            sha256_hash.update(chunk)

    return sha256_hash.hexdigest()

# Path to the file to calculate the SHA-256 hash
file_path = 'text.txt'

# Calculate the SHA-256 hash of the original file
original_hash = '9ee7c7e3da8390ad34e3d2affe186b9d2b5b5e13da81a5fe6547ca57d9ed37ff'
print("Original SHA-256 Hash:", original_hash)

# Calculate the SHA-256 hash of the modified file
modified_hash = calculate_sha256(file_path)
print("Modified SHA-256 Hash:", modified_hash)








# Message-1 md5
with open('message1.bin', 'rb') as file:
    binary_data = file.read()
def calculate_md5(data):
        sha256_hash = hashlib.md5()
        sha256_hash.update(data)
        return sha256_hash.hexdigest()

# Example usage
input_data = "Hello, world!"  # Can be a string or binary data
md5_result = calculate_md5(binary_data)
print("md5:", md5_result)


# Message-1 SHA-1
with open('message1.bin', 'rb') as file:
    binary_data = file.read()
def calculate_sha1(data):
        sha1_hash = hashlib.sha1()
        sha1_hash.update(data)
        return sha1_hash.hexdigest()

# Example usage
input_data = "Hello, world!"  # Can be a string or binary data
sha1_result = calculate_sha1(binary_data)
print("sha1:", sha1_result)






# Message-1 md5
with open('message2.bin', 'rb') as file:
    binary_data = file.read()
def calculate_md5(data):
        sha256_hash = hashlib.md5()
        sha256_hash.update(data)
        return sha256_hash.hexdigest()

# Example usage
input_data = "Hello, world!"  # Can be a string or binary data
md5_result = calculate_md5(binary_data)
print("md5:", md5_result)


# Message-1 SHA-1
with open('message2.bin', 'rb') as file:
    binary_data = file.read()
def calculate_sha1(data):
        sha1_hash = hashlib.sha1()
        sha1_hash.update(data)
        return sha1_hash.hexdigest()

# Example usage
input_data = "Hello, world!"  # Can be a string or binary data
sha1_result = calculate_sha1(binary_data)
print("sha1:", sha1_result)







    
    
    
    
    
    
    
    


