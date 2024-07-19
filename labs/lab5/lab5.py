
import hashlib
#  84932be2d2c362fd5bd0e1b47b014d500ea4b1858a14748a0ea963b8fdb59e2c
def calculateHash(a):
    return hashlib.sha256(a).hexdigest()

def merkleTree(file):
    with open(file, "rb") as data:
        content = data.read()
        block_len = 1024
        block_size = len(content) // block_len
        dataBlock = [content[i:i+block_size] for i in range(0, len(content), block_size)]

        block = []
        for i in dataBlock:
            block.append(calculateHash(i))

        while len(block) > 1:
            block_2=[]
            for i in range(0, len(block), 2):
                concatenate = block[i] + block[i + 1] if  i + 1< len(block) else block[i]
                hash = calculateHash(concatenate.encode())
                block_2.append(hash)
            block = block_2    
        if block:
            return block[0]
        else:
            return None

file = 'Lab7-6-2023.pdf'
print(merkleTree(file))

