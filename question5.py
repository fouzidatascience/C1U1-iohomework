# Question 5: Check if the name x is in the file

file = open('./student_names.txt')
x = input("What word are you looking for? ")
if (x in file.read()):
    print("Word found.")
else:
    print("Word not found.")