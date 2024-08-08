def generate_key_matrix(key):
    key = key.replace(" ", "").upper()
    key_matrix = []
    for char in key:
        if char not in key_matrix:
            key_matrix.append(char)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)
    
    # Convert the flat list into a 5x5 matrix
    key_matrix_2d = [key_matrix[i:i + 5] for i in range(0, len(key_matrix), 5)]
    return key_matrix_2d

def prepare_input(text):
    text = text.upper().replace(" ", "")
    prepared_text = ""
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            prepared_text += text[i] + "X"
        elif text[i] == text[i + 1]:
            prepared_text += text[i] + "X"
        else:
            prepared_text += text[i] + text[i + 1]
            i += 1
        i += 1
    return prepared_text

def find_position(key_matrix, letter):
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                return i, j
    return None, None

def encrypt(plain_text, key):
    key_matrix = generate_key_matrix(key)
    prepared_text = prepare_input(plain_text)
    encrypted_text = ""
    for i in range(0, len(prepared_text), 2):
        char1 = prepared_text[i]
        char2 = prepared_text[i + 1]
        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)
        if row1 == row2:
            encrypted_text += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]
    return encrypted_text

# Example usage
plain_text = input("Enter the plain text: ")
key = input("Enter the key: ")
encrypted_text = encrypt(plain_text, key)
print("Encrypted text:", encrypted_text)