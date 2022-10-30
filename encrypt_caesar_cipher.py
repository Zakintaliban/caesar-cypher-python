"""Kodingan ini untuk mempelajari kriptografi encrypt pada caesar cipher"""
import string

# input kata untuk di encrypt dan menjadi lower text
plain_text = (input("Enter the plain text: ").lower())
# masukan berapa angka untuk diputar
shift = int(input("Enter the shift: "))
# karena ALPHABETS hanya terdapat 26 huruf maka kita gunakan modulus
shift %= 26
# membuat list ALPHABETS
ALPHABETS = string.ascii_lowercase
"""
membuat list ALPHABETS diputar jadi contoh,
abcdefghijklmnopqrstuvwxyz di beri shift 3, menjadi
defghijklmnopqrstuvwxyzabc
"""
shifted = ALPHABETS[shift:] + ALPHABETS[:shift]
# guna maketrans ialah mengganti huruf yang di input
# dengan huruf yang sudah diputar (contoh, a menjadi d)
tableshift = str.maketrans(ALPHABETS, shifted)
# mengksekusikan plain/decrypt text menjadi shifted/encrypt text
encrypted = plain_text.translate(tableshift)
# hasil encrypt
print(encrypted)
