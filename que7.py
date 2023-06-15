#Write a python program to find the longest words.

list = ["dhrumi","soni","sakshi"]
longest_word = ""
for word in list:
    if len(word) >len(longest_word):
        longest_word = word

print("longest word:",longest_word)    