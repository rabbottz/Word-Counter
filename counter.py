'''
CPSC427
Team Member 1: Andrew Abbott
Submitted By: Andrew Abbott
GU Username: aabbott
File Name: prog2.py
Program reads and determines word count broken down by letter of a file that is specified by the user.
To Execute: python prog2.py
Python Version 2.7.10
'''
import re

'''
pre: none
post: the file specified by the user is opened
'''
def file_open():
    while(True):
        fileName = raw_input("What file would you like to count? (enter with the desired file type) ")
        try:
            fin = open(fileName, "r")
            break
        except:
            print("Invalid file name, Try again")
    return fin, fileName

'''
pre: string is a string
post: returns a string containing all characters in string_in that are also
    in good_chars, namely lower case alphabetic characters and spaces while removing
    words that contain any bad characters like " and, " or " end. ". Tokenize also removes
    words that start with a bad letter like ("when) . 
'''
def tokenize(string_in):
    string = re.sub('\n',' ', string_in)
     #create a list containing all lower case characters
    good_chars = [chr(value) for value in range(ord('a'),ord('z') + 1,1)]
    good_chars.append(' ') #add space to good characters so that it's retained
                           #see split in freq_table, below
    string = string.lower()
    new_str = ''
    temp_str = ''
    isBadChar = False
    isHold = False
    isConj = False
    for ch in string:
        if ch in good_chars:
            temp_str = temp_str + ch
            if ch == ' ' and not isHold and not isBadChar:
                new_str = new_str + temp_str
                del temp_str
                temp_str = ''
                isBadChar = False
                isHold = False
            elif ch == ' ' and isHold:
                del temp_str
                temp_str = ''
                isBadChar = False
                isHold = False
            elif ch == ' ' and isBadChar:
                del temp_str
                temp_str = ''
                isBadChar = False
                isHold = False
            elif ch != ' ' and isBadChar:
                isConj = True
                isBadChar = False
        else:
            if not temp_str:
                isHold = True
            elif len(temp_str) > 1 and not isBadChar:
                isBadChar = True
            elif isBadChar:
                isHold = True
    return new_str

'''
pre: string_in is a string
post: returns a dictionary where the key is an element of string_in and the
    value is the number of times it appears in string_in
'''
def freq_table(string_in):
    count_dict = {}
    word_lst = string_in.split()
    for word in word_lst:
        if word[0] in count_dict:
            count_dict[word[0]] = count_dict[word[0]] + 1
        else:
            count_dict[word[0]] = 1
    return count_dict

'''
pre: count_dict is the dictionary created in the function freq_table
post: writes the the key/value pairs of count_dict to a file
'''
def print_freq(count_dict, fileName):
    word_lst = list(count_dict.keys())
    word_lst.sort()
    print("\nWord count in " + fileName + " by letter. \n")
    print("CHARACTER    FREQUENCY\n")
    for word in word_lst:
        print(word + ':\t\t' + str(count_dict[word]) + '\n')

def main():
    
    fin, fileName = file_open()
    content_raw = fin.read()
    content_cooked = tokenize(content_raw)
    dictionary_count = freq_table(content_cooked)
    print_freq(dictionary_count, fileName)
    fin.close()

main()
