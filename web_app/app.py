from flask import Flask, render_template, request
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from collections import Counter

app = Flask(__name__)

class ShiftCipher:
    def __init__(self):
        self.shift = 3  # Default shift value
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def set_shift(self, shift):
        """Set the shift value"""
        self.shift = shift
    
    def encrypt(self, plaintext):
        """Encrypt plaintext using shift cipher"""
        ciphertext = []
        process_steps = []
        
        for char in plaintext.upper():
            if char in self.alphabet:
                original_pos = self.alphabet.index(char)
                new_pos = (original_pos + self.shift) % 26
                encrypted_char = self.alphabet[new_pos]
                ciphertext.append(encrypted_char)
                
                # Detailed steps showing the shift process
                step = f"{char} ({original_pos}) → {encrypted_char} ({new_pos}) [Shift +{self.shift}]"
                process_steps.append(step)
            else:
                ciphertext.append(char)
                process_steps.append(f"{char} → (unchanged)")
        
        return ''.join(ciphertext), process_steps
    
    def decrypt(self, ciphertext):
        """Decrypt ciphertext using shift cipher"""
        plaintext = []
        process_steps = []
        
        for char in ciphertext.upper():
            if char in self.alphabet:
                original_pos = self.alphabet.index(char)
                new_pos = (original_pos - self.shift) % 26
                decrypted_char = self.alphabet[new_pos]
                plaintext.append(decrypted_char)
                
                # Detailed steps showing the shift process
                step = f"{char} ({original_pos}) → {decrypted_char} ({new_pos}) [Shift -{self.shift}]"
                process_steps.append(step)
            else:
                plaintext.append(char)
                process_steps.append(f"{char} → (unchanged)")
        
        return ''.join(plaintext), process_steps
    
    def brute_force(self, ciphertext):
        """Perform brute force attack on ciphertext"""
        results = []
        
        for potential_shift in range(1, 26):
            test_cipher = ShiftCipher()
            test_cipher.set_shift(potential_shift)
            decrypted, _ = test_cipher.decrypt(ciphertext)
            results.append({
                'shift': potential_shift,
                'text': decrypted[:50] + '...' if len(decrypted) > 50 else decrypted
            })
            
        return results

# Initialize cipher with default shift
cipher = ShiftCipher()

@app.route('/', methods=['GET', 'POST'])
def index():
    encryption_result = ""
    decryption_result = ""
    encrypt_steps = []
    decrypt_steps = []
    brute_force_results = []
    shift = 3  # Default shift value
    
    if request.method == 'POST':
        shift = int(request.form.get('shift', 3))
        cipher.set_shift(shift)
        
        if 'encrypt' in request.form:
            plaintext = request.form.get('plaintext', '')
            if plaintext:
                ciphertext, encrypt_steps = cipher.encrypt(plaintext)
                encryption_result = ciphertext
        
        if 'decrypt' in request.form:
            ciphertext = request.form.get('ciphertext', '')
            if ciphertext:
                plaintext, decrypt_steps = cipher.decrypt(ciphertext)
                decryption_result = plaintext
        
        if 'brute_force' in request.form:
            ciphertext = request.form.get('ciphertext', '')
            if ciphertext:
                brute_force_results = cipher.brute_force(ciphertext)
    
    return render_template('index.html', 
                         encryption_result=encryption_result,
                         decryption_result=decryption_result,
                         encrypt_steps=encrypt_steps,
                         decrypt_steps=decrypt_steps,
                         brute_force_results=brute_force_results,
                         shift=shift)

if __name__ == '__main__':
    app.run(debug=True)