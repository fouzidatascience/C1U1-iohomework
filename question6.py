# Question 6: Generate 26 text file named A.txt, B.txt up to Z.txt


# Alphabet in caps being between 65 and 91 (excluded) in the ASCII table, we use them as range and get the letters back using chr

for i in range(65,91):
    name = './' + chr(i) + '.txt'
    f = open(name,'x') # x for exclusive creation so it doesn't create a new file if it already exits
    f.close() 