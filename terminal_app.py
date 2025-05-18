import matplotlib.pyplot as plt
from collections import Counter

class ShiftCipher:
    def __init__(self, shift=3):
        self.shift = shift
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def encrypt(self, plaintext):
        ciphertext = []
        for char in plaintext.upper():
            if char in self.alphabet:
                index = (self.alphabet.index(char) + self.shift) % 26
                ciphertext.append(self.alphabet[index])
            else:
                ciphertext.append(char)
        return ''.join(ciphertext)
    
    def decrypt(self, ciphertext):
        plaintext = []
        for char in ciphertext.upper():
            if char in self.alphabet:
                index = (self.alphabet.index(char) - self.shift) % 26
                plaintext.append(self.alphabet[index])
            else:
                plaintext.append(char)
        return ''.join(plaintext)
    
    def display_shift_alphabet(self):
        """Display the shifted alphabet mapping"""
        print("\nAlphabet Mapping:")
        print("Plaintext:  " + self.alphabet)
        
        shifted = ''.join([self.alphabet[(i + self.shift) % 26] for i in range(26)])
        print("Ciphertext: " + shifted)
        print()
    
    def brute_force(self, ciphertext):
        """Try all possible shifts (1-25) to decrypt the message"""
        print("\n=== Brute Force Attack ===")
        print("Trying all possible shifts (1-25):")
        
        for test_shift in range(1, 26):
            test_cipher = ShiftCipher(test_shift)
            decrypted = test_cipher.decrypt(ciphertext)
            print(f"Shift {test_shift:2}: {decrypted[:50]}" + ("..." if len(decrypted) > 50 else ""))

def display_encryption_process(plaintext, shift):
    cipher = ShiftCipher(shift)
    cipher.display_shift_alphabet()
    
    ciphertext = ""
    print("=== Encryption Process ===")
    print(f"Shift Value: {shift}")
    print(f"Plaintext:  {plaintext}")
    
    print("\nStep-by-step encryption:")
    for char in plaintext.upper():
        if char in cipher.alphabet:
            original_pos = cipher.alphabet.index(char)
            new_pos = (original_pos + shift) % 26
            encrypted_char = cipher.alphabet[new_pos]
            ciphertext += encrypted_char
            print(f"{char} (position {original_pos}) → {encrypted_char} (position {new_pos}) [Shift +{shift}]")
        else:
            ciphertext += char
            print(f"{char} → {char} (unchanged)")
    
    print(f"\nFinal Result: {ciphertext}")

def display_decryption_process(ciphertext, shift):
    cipher = ShiftCipher(shift)
    cipher.display_shift_alphabet()
    
    plaintext = ""
    print("=== Decryption Process ===")
    print(f"Shift Value: {shift}")
    print(f"Ciphertext: {ciphertext}")
    
    print("\nStep-by-step decryption:")
    for char in ciphertext.upper():
        if char in cipher.alphabet:
            original_pos = cipher.alphabet.index(char)
            new_pos = (original_pos - shift) % 26
            decrypted_char = cipher.alphabet[new_pos]
            plaintext += decrypted_char
            print(f"{char} (position {original_pos}) → {decrypted_char} (position {new_pos}) [Shift -{shift}]")
        else:
            plaintext += char
            print(f"{char} → {char} (unchanged)")
    
    print(f"\nFinal Result: {plaintext}")

if __name__ == "__main__":
    print("Shift Cipher (Caesar Cipher) System")
    print("==================================")
    print("\nA shift cipher works by shifting each letter in the plaintext")
    print("by a fixed number of positions in the alphabet.")
    print("With only 25 possible keys, it's vulnerable to brute force attacks.")
    
    while True:
        print("\nOptions:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Brute Force Attack")
        print("4. Exit")
        
        choice = input("Select option (1-4): ")
        
        if choice == '1':
            plaintext = input("Enter plaintext to encrypt: ")
            shift = int(input("Enter shift value (1-25): "))
            display_encryption_process(plaintext, shift)
            
        elif choice == '2':
            ciphertext = input("Enter ciphertext to decrypt: ")
            shift = int(input("Enter shift value (1-25): "))
            display_decryption_process(ciphertext, shift)
            
        elif choice == '3':
            ciphertext = input("Enter ciphertext to attack: ")
            cipher = ShiftCipher()
            cipher.brute_force(ciphertext)
            
        elif choice == '4':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please select 1-4")