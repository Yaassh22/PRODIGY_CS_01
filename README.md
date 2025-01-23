# PRODIGY_CS_01

Caesar Cipher Program
This is a simple Python implementation of the Caesar Cipher encryption and decryption algorithm. The Caesar Cipher is one of the oldest and simplest methods of encryption, where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

Features
Encryption: The program allows the user to encrypt a message using a specified key.
Decryption: The program also enables decryption of a ciphertext using the same key that was used for encryption.
Alphabetic letters only: The program handles alphabetic letters (both uppercase and lowercase), while ignoring punctuation marks and other non-alphabet characters.
Space handling: Spaces are preserved in both encryption and decryption.
How It Works
Encryption:

The user is prompted to input a text message and an encryption key (a number between 1 and 26).
Each letter in the message is shifted by the key value, creating the encrypted message.
Decryption:

The user is prompted to input a ciphertext and the same key used for encryption.
The program shifts the letters in the opposite direction to recover the original message.
Wrap-around:

If the shift moves past 'z' during encryption or before 'a' during decryption, the letters will wrap around to the start or end of the alphabet.
Usage
Clone or download the repository to your local machine.
Run the caesar_cipher.py script in your Python environment.
The program will prompt you to select between encryption or decryption mode.
Enter the required details (key and text) and the program will output the encrypted or decrypted message.
