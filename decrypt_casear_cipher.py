"""Kodingan ini untuk mempelajari kriptografi decrypt pada caesar cipher"""
import string

# input kata untuk di encrypt dan menjadi lower text
encrypted = (input("Enter the encrypted text: ").lower())
# masukan berapa angka untuk diputar
shift = int(input("Enter the shift: "))
# karena ALPHABETS hanya terdapat 26 huruf maka kita gunakan modulus
shift %= 26
# membuat list of ALPHABETS
ALPHABETS = string.ascii_lowercase
"""
kebalikan dari shifted, mereka mundur,
dari defghijklmnopqrstuvwxyzabc menjadi
abcdefghijklmnopqrstuvwxyz ketika dimundur 3
"""
unshifted = ALPHABETS[-shift:] + ALPHABETS[:-shift]
"""
guna maketrans ialah mengganti huruf yang ter-encrypted
dengan huruf yang akan dimundur (contoh, d menjadi a)
"""
tableunshift = str.maketrans(ALPHABETS, unshifted)
# mengksekusikan shifted/encrypt text menjadi plain/decrypt text
decrypted = encrypted.translate(tableunshift)
# hasil decrypt
print(decrypted)
