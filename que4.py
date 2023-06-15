#Write a Python program to read last n lines of a file.

f= open("term1.txt","r")
n= int(input("number of a file to read:"))
l1 = f.readlines()[n:]
for i in l1:
    print(i)