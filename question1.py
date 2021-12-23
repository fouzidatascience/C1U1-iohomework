# Question 1 : Read all of the content of the file in one variable

file = open('./student_names.txt')
names = file.read()
print(names)

file.close()
