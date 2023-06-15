#Write a Python program to write a list to a file.
my_list = [1, 2, 3, 4, 5]
file_path = 'terms5.txt'

with open(file_path, 'w') as file:
    for item in my_list:
        file.write(str(item) + '\n')

