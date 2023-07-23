import hashlib

def calculate_hash(data):
    return hashlib.sha256(data).hexdigest()

def build_merkle_tree(filePath):

    with open(filePath,'rb') as file:
        fileContent = file.read()
        blockSize = len(fileContent)//1024
        dataBlock = [fileContent[i:i+blockSize] for i in range(0, len(fileContent),blockSize)]

        blockHashes = []

        for data in dataBlock:
            blockHashes.append(calculate_hash(data))

    
    while len(blockHashes) > 1:
        next_level = []

        for i in range(0, len(blockHashes), 2):
            concatenated = blockHashes[i] + blockHashes[i + 1] if i + 1 < len(blockHashes) else blockHashes[i]
            hash_value = calculate_hash(concatenated.encode())
            next_level.append(hash_value)
        
        blockHashes = next_level
    
    return blockHashes[0] if blockHashes else None

filePath = 'Lab 7-6-2023.pdf'
merkle_root = build_merkle_tree(filePath)
print("Merkle Root:", merkle_root)