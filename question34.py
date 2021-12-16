
# We open the file for both question
file = open('./student_names.txt')



# Question 3: Read the first n lines of the file

# First we read n 
n = input("Enter N: ")
output = file.readlines()[:n]
print(output)


# Question 4: Read the last n lines of the file

# We read n from I/O
n = input("Enter N: ")
output = file.readlines()[-n:]
print(output)



file.close()