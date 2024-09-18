# Implement ECDSA in Netbeans 8.2

import ecdsa
import os

def generate_keypair():
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)
    public_key = private_key.get_verifying_key()
    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(message.encode())
    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(signature, message.encode())
        return True
    except ecdsa.BadSignatureError:
        return False

def main():
    private_key, public_key = generate_keypair()

    message = "Hello, ECDSA!"
    print(f"Original message: {message}")

    signature = sign_message(private_key, message)
    print(f"Signature: {signature.hex()}")

    is_valid = verify_signature(public_key, message, signature)
    print(f"Signature is valid: {is_valid}")

    tampered_message = "Hello, ECDSA tampered!"
    is_valid_tampered = verify_signature(public_key, tampered_message, signature)
    print(f"Tampered message signature is valid: {is_valid_tampered}")

    with open("private_key.pem", "wb") as f:
        f.write(private_key.to_pem())

    with open("public_key.pem", "wb") as f:
        f.write(public_key.to_pem())

    with open("private_key.pem", "rb") as f:
        loaded_private_key = ecdsa.SigningKey.from_pem(f.read())

    with open("public_key.pem", "rb") as f:
        loaded_public_key = ecdsa.VerifyingKey.from_pem(f.read())

    new_message = "Testing loaded keys"
    new_signature = sign_message(loaded_private_key, new_message)
    is_valid_loaded = verify_signature(loaded_public_key, new_message, new_signature)
    print(f"Signature with loaded keys is valid: {is_valid_loaded}")

if __name__ == "__main__":
    main()