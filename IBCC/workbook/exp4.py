#  Implement SHA-256 in Netbeans 8.2

import hashlib

def sha256_hash(input_string):
    input_bytes = input_string.encode('utf-8')
    sha256 = hashlib.sha256()
    sha256.update(input_bytes)
    return sha256.hexdigest()

input_text = "Hello, World!"
hash_result = sha256_hash(input_text)
    
print(f"Input: {input_text}")
print(f"SHA-256 Hash: {hash_result}")

while True:
    user_input = input("\nEnter text to hash (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
       break
    hash_result = sha256_hash(user_input)
    print(f"SHA-256 Hash: {hash_result}")