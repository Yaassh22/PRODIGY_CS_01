letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)

# Function to encrypt or decrypt text based on the mode and key
def encrypt_decrypt(text, mode, key):
    result = ""
    if mode == 'd':
        key = -key  # Reverse the key for decryption
    
    for letter in text:
        letter = letter.lower()
        if letter in letters:  # Encrypt/Decrypt only alphabetic letters
            index = letters.find(letter)
            new_index = index + key
            if new_index >= num_letters:
                new_index -= num_letters  # Wrap around if it exceeds the alphabet length
            elif new_index < 0:
                new_index += num_letters  # Wrap around for negative index
            result += letters[new_index]
        elif letter == " ":  # Maintain spaces
            result += " "
        # Ignore punctuation marks and do not include them in the result
    
    return result


print("\nCAESAR CIPHER PROGRAM\n")

print("Do you want to ENCRYPT or DECRYPT")
user_input = input("E/D: ").lower()
print()

if user_input == 'e':
    print("ENCRYPTION MODE SELECTED\n")
    key = int(input("Enter the key (1 to 26): "))
    text = input("Enter the text to Encrypt: ")
    ciphertext = encrypt_decrypt(text, user_input, key)
    print(f"CIPHERTEXT: {ciphertext}")

elif user_input == 'd':
    print("DECRYPTION MODE SELECTED\n")
    key = int(input("Enter the key (1 to 26): "))
    text = input("Enter the text to Decrypt: ")
    plaintext = encrypt_decrypt(text, user_input, key)
    print(f"PLAINTEXT: {plaintext}")

else:
    print("Invalid choice! Please select 'E' for Encrypt or 'D' for Decrypt.") 
