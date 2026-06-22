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

print ("===========================")

word = ["P", "Y", "T", "H", "O", "N"]

n = 4
number = 0
for i in range (n):
    for j in range (i):
        print (word[number], end = " ")
        number = number + 1
    print (" ")

print ("===============================")

n = 7
number = 0
for i in range (n):
    for j in range (i):
        print (word[number], end = " ")
        number = number + 1
    print (" ")
    number = 0

print ("============================")

n = 27
number = 0
for i in range (n):
    for j in range (i):
        print (Alphabet[number], end = " ")
        number = number + 1
    print (" ")
    number = 0

n = 27
number = 0
for i in range (n-1,0, -1):
        print ((n-i)*" ", end = " ")
        print (i *(Alphabet[number]))
        number = 0
print ("=================================")

letter = "Z"
n = Alphabet.index(letter) + 1
for i in range (1,n + 1):
    print ((n-i)*" ", end = "")
    for j in range (i):
        print (f"{Alphabet[j]}", end = " ")
    print ()
# the first line below the for loop is trying to create all the spaces
#  the next line is the loop which in it shows what alphabet you would like to print and as many times starting from "A" going up 
# the n is the index it would like to go to and the letter is just the simpler form of n.

"""
   A 
  B C 
 D E F
G H I J
"""

alphabet_number = 0
n = 5
for i in range (n):
    print ((n-i)* " ", end = "")
    for j in range (i):
        print (Alphabet[alphabet_number], end = " ")
        alphabet_number = alphabet_number + 1
    print (" ")

