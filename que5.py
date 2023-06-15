#Write a Python program to read a file line by line and store it into a list

file_path = "term2.txt"
n = int(input("enter the numbers of lines to read:"))

file = open(file_path,"r")
lines = file.readlines()
file.close()

lines = lines[:n]

print(lines)