"""
A
B C
D E F
G H I J

HINT: Store letters a to z in a list.
"""
Alphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
alphabet_number = 0
n = 5
for i in range (n):
    for j in range (i):
        print (Alphabet[alphabet_number], end = " ")
        alphabet_number = alphabet_number + 1
    print (" ")