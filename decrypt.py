from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad
import os

def decrypt_file(file_path, key, iv):
    with open(file_path, 'rb') as file:
        encrypted_content = file.read()
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted_content = unpad(cipher.decrypt(encrypted_content), DES3.block_size)
    decrypted_file_path = file_path + ".jpeg"
    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_content)

# Key and IV
key = b"Lp3jXluuW799rnu4"  # 16 bytes key
iv = bytes([0, 1, 2, 3, 4, 5, 6, 7])  # 8 bytes IV
#file_path = r"C:\Users\XIII\Downloads\saveme-chall\images (144).png"
file_path = r"C:\Users\XIII\Downloads\image\something.png"
decrypt_file(file_path, key, iv)
