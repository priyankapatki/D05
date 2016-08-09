#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def word_read():
    open_file = open('words.txt', 'r')
    line = open_file.readline()   

    for line in open_file:
        rem_space = line.replace(' ', '')   # removes spaces from the word by replacing it by ''
        word = rem_space.strip('\n')         # removes the trailing \n
        if len(word) > 20:
            print(word + ' '+ str(len(word))  # prints words with more than 20 characters



##############################################################################
def main():
    
    word_read()
if __name__ == '__main__':
    main()
