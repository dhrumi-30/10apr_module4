#Write a Python program to append text to a file and display the text.

file1 = "myblank_file.txt"
file = open(file1,"a")

name = input("enter the data:")

file.write(name + "\n")

file.close()