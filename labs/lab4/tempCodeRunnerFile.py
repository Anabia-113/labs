for i in range(0, 8, 2):
        hash = blocks[i] + blocks[i + 1]
        hash = hl.sha256(hash.encode()).hexdigest()
        block_4.append(hash)