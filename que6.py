#Write a Python program to read a file line by line store it into a variable.4


file_path = "term3.txt"
n = int(input("enter the numbers of lines to read:"))

file = open(file_path,"r")
lines = file.readlines()
file.close()

lines = lines[:n]

print(lines)
