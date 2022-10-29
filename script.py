import string

# input kata untuk di encrypt dan menjadi lower text
plain_text = (input("Enter the plain text: ").lower())
# masukan berapa angka untuk diputar
shift = int(input("Enter the shift: "))
# karena alphabets hanya terdapat 26 huruf maka kita gunakan modulus
shift %= 26

# membuat list alphabets
alphabets = string.ascii_lowercase
# membuat list alphabets diputar jadi contoh, abcdefghijklmnopqrstuvwxyz di beri shift 3, menjadi defghijklmnopqrstuvwxyzabc
shifted = alphabets[shift:] + alphabets[:shift]
# guna maketrans ialah mengganti huruf yang di input dengan huruf yang sudah diputar (contoh, a menjadi d)
tableshift = str.maketrans(alphabets, shifted)
# mengksekusikan plain/decrypt text menjadi shifted/encrypt text
encrypted = plain_text.translate(tableshift)
# hasil encrypt
print(encrypted)

# kebalikan dari shifted, mereka mundur, dari defghijklmnopqrstuvwxyzabc menjadi abcdefghijklmnopqrstuvwxyz ketika dimundur 3
unshifted = alphabets[-shift:] + alphabets[:-shift]
tableunshift = str.maketrans(alphabets, unshifted)
# mengksekusikan shifted/encrypt text menjadi plain/decrypt text
decrypted = encrypted.translate(tableunshift)
# hasil encrypt
print(decrypted)