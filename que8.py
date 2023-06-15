#Write a Python program to count the number of lines in a text file.


f= open("term4.txt","r")
l1=f.readlines()

line_count = len(l1)
f.close()

print(line_count)