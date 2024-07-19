import hashlib as hl
# task 1
print("paragraph 1 hash: 1d0ada7a906e529d19fb2aca66911eaaee84ff4c7c6b685f019cd79c2deec5ff")
print("paragraph 2 hash: 6c8ed1b6a6745bc64645ce63e23c9258545de0bf1c3c8efdfb3fad46d5d1fb6c")
print("paragraph 3 hash: c43194ab05fca649152ea3b92c49eacee99902badd7ea503e3315d49a83781ba")
print("paragraph 4 hash: b349939cb094a89e4cf720b895df300c0d5c7b3f0f3a237bc026cad42637fb61")
print("paragraph 1 and 2 hash: a1d1f83cb2b5fcf557e6cae6962774ebfba159cea5d43c4a8ebb61a02a7a67bf")
print("paragraph 3 & 4 hash: 02d937710a779508721c03e1637064e652d183a4e5d1da28d0f25538c4bcaf9b")
print("merkle root hash: 448ec525a32f5f92dd9ef89c40829d0eb7c2edd59cb1639b92aea49af1ba76bc")

# task 2

data_A = 'a'
data_B = 'b'
data_C = 'c'

data_D = 'd'
data_E = 'e'
data_F = 'f'
data_G = 'g'
data_H = 'h'

hash_A = hl.sha256(data_A.encode()).hexdigest()
hash_B = hl.sha256(data_B.encode()).hexdigest()
hash_C = hl.sha256(data_C.encode()).hexdigest()
hash_D = hl.sha256(data_D.encode()).hexdigest()
hash_E = hl.sha256(data_E.encode()).hexdigest()
hash_F = hl.sha256(data_F.encode()).hexdigest()
hash_G = hl.sha256(data_G.encode()).hexdigest()
hash_H = hl.sha256(data_H.encode()).hexdigest()

hash_A_hash_B  = hl.sha256((hash_A + hash_B).encode()).hexdigest()
hash_C_hash_D  = hl.sha256((hash_C + hash_D).encode()).hexdigest()
hash_E_hash_F  = hl.sha256((hash_E + hash_F).encode()).hexdigest()
hash_G_hash_H  = hl.sha256((hash_G + hash_H).encode()).hexdigest()

hash_A_hash_B_hash_C_hash_D = hl.sha256((hash_A_hash_B + hash_C_hash_D).encode()).hexdigest()
hash_E_hash_F_hash_G_hash_H = hl.sha256((hash_E_hash_F + hash_G_hash_H).encode()).hexdigest()

print("Markle Tree : ", hl.sha256((hash_A_hash_B_hash_C_hash_D + hash_E_hash_F_hash_G_hash_H).encode()).hexdigest())


# Task 3

with open("Lab5-6-2023.pdf", "r") as file:
        contents = file.read()
        file_size = len(contents)
        block_size = file_size // 8

print(len(block_size))


    
            

    
    
