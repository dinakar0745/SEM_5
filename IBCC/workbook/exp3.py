# Implement Elliptic curve cryptography (ECC) Key generation, encryption and decryption.

import secrets
from tinyec import registry
from tinyec.ec import Point
import hashlib

def compress_point(point):
    return hex(point.x) + hex(point.y % 2)[2:]

def point_to_key(point):
    sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
    sha.update(int.to_bytes(point.y, 32, 'big'))
    return sha.digest()

def encrypt(msg, pubKey):
    privKey = secrets.randbelow(curve.field.n)
    sharedKey = privKey * pubKey
    secretKey = point_to_key(sharedKey)
    ciphertext = b''
    nonce = secrets.token_bytes(16)
    for i in range(len(msg)):
        ciphertext += bytes([msg[i] ^ secretKey[i % 32]])
    return (privKey * curve.g, nonce, ciphertext)

def decrypt(encryptedMsg, privKey):
    (pubKey, nonce, ciphertext) = encryptedMsg
    sharedKey = privKey * pubKey
    secretKey = point_to_key(sharedKey)
    msg = b''
    for i in range(len(ciphertext)):
        msg += bytes([ciphertext[i] ^ secretKey[i % 32]])
    return msg

curve = registry.get_curve('brainpoolP256r1')

def generate_key_pair():
    privKey = secrets.randbelow(curve.field.n)
    pubKey = privKey * curve.g
    return privKey, pubKey

# Example usage
privKey, pubKey = generate_key_pair()
print("Private Key:", hex(privKey))
print("Public Key:", compress_point(pubKey))

msg = b'This is a secret message.'
encrypted = encrypt(msg, pubKey)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, privKey)
print("Decrypted:", decrypted.decode())