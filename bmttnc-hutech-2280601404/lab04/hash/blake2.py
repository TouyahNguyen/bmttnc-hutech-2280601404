import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message)
    return blake2_hash.digest()

if __name__ == "__main__":
    text = input("Nhập chuỗi cần băm: ").encode('utf-8')
    hashed_text = blake2(text)
    print("BLAKE2 Hash:", hashed_text.hex())
