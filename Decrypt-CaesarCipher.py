import string

# input kata untuk di encrypt dan menjadi lower text
encrypted = (input("Enter the encrypted text: ").lower())
# masukan berapa angka untuk diputar
shift = int(input("Enter the shift: "))
# karena alphabet hanya terdapat 26 huruf maka kita gunakan modulus
shift %= 26

# membuat list of alphabets
alphabets = string.ascii_lowercase

# kebalikan dari shifted, mereka mundur, dari defghijklmnopqrstuvwxyzabc menjadi abcdefghijklmnopqrstuvwxyz ketika dimundur 3
unshifted = alphabets[-shift:] + alphabets[:-shift]
# guna maketrans ialah mengganti huruf yang ter-encrypted dengan huruf yang akan dimundur (contoh, d menjadi a)
tableunshift = str.maketrans(alphabets, unshifted)
# mengksekusikan shifted/encrypt text menjadi plain/decrypt text
decrypted = encrypted.translate(tableunshift)
# hasil decrypt
print(decrypted)
