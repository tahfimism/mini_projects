

key = "xyzabcdefghijklmnopqrstuvw"

def encrypt(plaintext):
    ciphertext = []
    for char in plaintext.lower():
        ch = char(ord(char) - ord('a'))
        ciphertext.append(ch)
    
    return ''.join(char for char in ciphertext)
    

def decrypt(ciphertext):
    plaintext = []


def main():
    message = "Hello, World!"
    encrypted_message = encrypt(message)
    print(f"Encrypted: {encrypted_message}")
    
    #decrypted_message = decrypt(encrypted_message)
    #print(f"Decrypted: {decrypted_message}")


if __name__ == "__main__":
    main()