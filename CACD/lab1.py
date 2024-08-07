def encrypt(message, key):
    encrypted = ""
    key = ord(key.upper()) - ord('A')
    for char in message.upper():
        if char.isalpha():
            encrypted += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            encrypted += char
    return encrypted

def decrypt(message, key):
    decrypted = ""
    key = ord(key.upper()) - ord('A')
    for char in message.upper():
        if char.isalpha():
            decrypted += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        else:
            decrypted += char
    return decrypted

def main():
    message = input("Enter the msg: ")
    key = input("Enter key: ")

    encrypted = encrypt(message, key)
    print("The encrypted msg is", encrypted)

    decrypted = decrypt(encrypted, key)
    print("The decrypted msg is:", decrypted)

if __name__ == "__main__":
    main()
