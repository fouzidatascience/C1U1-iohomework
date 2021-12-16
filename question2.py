
# Question 2: Write a list of random names to the file

# We assume that we have a list of names

nameList = []


file = open('./student_names.txt','a') # We use 'a' mode: append, to add to the end of the file and not overwrite it
file.writelines(nameList)

file.close()



