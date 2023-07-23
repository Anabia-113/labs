import hashlib
# part1= '69ef5e51e1a3ba667bf396ae494e6b82ba7e891a05f37f66c770f067104e7397'
# part2= '40791afdc85ba029dc28348174e5bd5070dd664a421234f7a935a62d43f7852f'
# part3= '1e1b9dbeb353e6728457945cc47dac1a0121a3089bacf01650059bab0bfe92b6'
# part4= 'a2e895d7a586b90fd437784729a5e7f5d53ec1e5fef87805800ffb443eabba26'


# hash1 = "69ef5e51e1a3ba667bf396ae494e6b82ba7e891a05f37f66c770f067104e7397"
# hash2 = "40791afdc85ba029dc28348174e5bd5070dd664a421234f7a935a62d43f7852f"

# # Concatenate the two hashes
# combined_hash = '8b60968b65b8d72a1e29b58946c53efad4b41ead250e637d3d49d563276025ed'

# # Apply SHA-256 hash function to the concatenated string
# final_hash = hashlib.sha256(combined_hash.encode()).hexdigest()

# print("Combined Hash:", final_hash)









# # task 2

# #function to calculate the hash of a given string
# def calculate_hash(string):
#     sha256 = hashlib.sha256()
#     sha256.update(string.encode('utf-8'))
#     return sha256.hexdigest()

# # Function to construct the Merkle tree and calculate the Merkle root
# def calculate_merkle_root(strings):
#     # Calculate the hashes of the original strings
#     hashes = [calculate_hash(string) for string in strings]
    
#     # Base case: if there's only one hash, return it as the Merkle root
#     if len(hashes) == 1:
#         return hashes[0]
    
#     # Recursive case: construct the Merkle tree
#     new_hashes = []
#     for i in range(0, len(hashes), 2):
#         # If the number of hashes is odd, duplicate the last hash
#         if i == len(hashes) - 1:
#             hashes.append(hashes[i])
        
#         # Calculate the hash of the concatenated pair of hashes
#         concat_hash = hashes[i] + hashes[i + 1]
#         new_hash = calculate_hash(concat_hash)
#         new_hashes.append(new_hash)
    
#     # Recursively calculate the Merkle root with the new hashes
#     return calculate_merkle_root(new_hashes)

# # Generate eight random strings
# random_strings = [
#     "Anabia",
#     "goofy",
#     "scroot",
#     "Ali",
#     "Hash",
#     "Algorithm",
#     "Blockchain",
#     "Intigrity"
# ]
# # Calculate and print the Merkle root of the tree
# merkle_root = calculate_merkle_root(random_strings)
# print("Merkle root:", merkle_root)








# task 3
# with open('Lab6-6-2023.pdf', 'rb') as file:
#     binary_data = file.read()
file = open("lab-6-6-2023.pdf", "rb")
content = file.read()
    
listOfHashes = []
listOfTwoShes = []
listOfFourShes = []
rootHash = ""


blockSize = len(content) // 8
dataBlocks = [content[i:i + blockSize] for i in range(0, len(content), blockSize)]



for x in range(len(dataBlocks)):
    stringToHash = hashlib.sha256(dataBlocks[x]).hexdigest()
    listOfHashes.append(stringToHash)

# Concatenating two hashes and finding the heash of the concatenated string and storing into array
for x in range(0, 8, 2):
    stringToHash = listOfHashes[x] + listOfHashes[x + 1]
    stringToHash = hashlib.sha256(stringToHash.encode()).hexdigest()
    listOfTwoShes.append(stringToHash)

for x in range(0, 4, 2):
    stringToHash = listOfTwoShes[x] + listOfTwoShes[x + 1]
    stringToHash = hashlib.sha256(stringToHash.encode()).hexdigest()
    listOfFourShes.append(stringToHash)

for x in range(0, 2, 2):
    rootHash = listOfFourShes[x] + listOfFourShes[x + 1]
    stringToHash = hashlib.sha256(stringToHash.encode()).hexdigest()
    rootHash = stringToHash

print(f"List of Hashes: {listOfHashes}")
print(f"List of Two Shes: {listOfTwoShes}")
print(f"List of Four Shes: {listOfFourShes}")
print("\n")
print(f"Root Hash: {rootHash}")



