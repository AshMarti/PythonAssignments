################################################################
#   Weekly Exercise 3: Word Frequency
#   CMPUT 274 Fall 2020
#
#   Ashley Davis - 1616898
################################################################

import sys
import os.path

"""safeopen() will determine whether the file exists in the directory,
and will ask for the user to input a new file name if there is no openable file
it will return the opened file and the file's name
input values:  *input_file_name - the name of the file that the program will open
return values: *input_file - contents of the opened file
               *input_file_name - the name of the file the program opened (may be changed)"""
def safeopen(input_file_name):
    while not os.path.isfile(input_file_name):
        print("Cannot read file. File does not exist.")
        input_file_name=input("Enter a file name: ")
    input_file=open(input_file_name,"r")
    return input_file,input_file_name

"""readfile_splitwords() will take the opened file and and read it line by line,
removing any newline characters, splitting the words into a list, and deleting 
any instances of empty sapce
input values:  *input_file_name - the name of the file that the program will open
return values: *all_words - list of all words in the text file (including duplicates)
               *input_file_name - the name of the file the program opened (may be changed)"""
def readfile_splitwords(input_file_name):
    input_file,input_file_name=safeopen(input_file_name)
    all_words=[]
    for line in input_file.readlines():
        line=line.strip()
        line=line.split(" ")
        while line.count("")>0:
            line.remove("")
        all_words.extend(line)
    return all_words,input_file_name

"""countwords() creates an empty dictionary and fills it line by line with new words
and the number of times that word appears, added a count of plus 1 to duplicate words
and assigning a value of 1 to new words in the dictionary
input values:  *all_words - list of all words in the text file (including duplicates)
               *number_of_words - len(all_words), total number of words in the file
return values: *count_diction - dictionary with word and total count of that word"""
def countwords(all_words,number_of_words):
    count_diction={}
    for word in range(number_of_words):
        if all_words[word] in count_diction:
            count_diction[all_words[word]]+=1
        else:
            count_diction.update({all_words[word]:1})
    return count_diction

"""alphabetize() takes the dictionary created in countwords() and sorts it
alphabetically, keeping the count with the proper key
input values:  *unsorted_dict - input of "count_diction", unalphabetized dictionary
return values: *organized_dict - alphabetized dictionary where keys are words and
                                the value is count of that word"""
def alphabetize(unsorted_dict):
    organized_dict={}
    for key in sorted(unsorted_dict.keys()):
        organized_dict.update({key:unsorted_dict[key]})
    return organized_dict

"""frequency() takes the alphabetized dictionary and finds the ratio that each word
appears relative to the other words by dividing the count of that word by the total
number of words and reounding it to three decimals. It stores these values in a list.
input values:  *organized_dict - alphabetized dictionary with words and their count
               *number_of_words - total number of words in the original text file
return values: *freq_list - returns frequency of each word in an organized list"""
def frequency(organized_dict,number_of_words):
    freq_list=list()
    count_of_word=list(organized_dict.values())
    for index in range(len(organized_dict)):
        freq_list.append(round((int(count_of_word[index])/number_of_words),3))
    return freq_list

"""write_output() is the main function. When called, it will call each of the other 
functions to generate a dictionary with words and their count, and then a list of
frequencies in the same order as the dictionary. The function then opens a new file
(or overwrites a pre-existing file) with the name {filename}.out and prints each word,
its count, and its frequency line by line into the file.
input values:  *input_file_name - the name of the file that the program will open
return values: *input_file_name - the name of the file the program opened (may be changed)"""
def write_output(input_file_name):
    all_words,input_file_name=readfile_splitwords(input_file_name)
    number_of_words=len(all_words)
    count_diction=countwords(all_words,number_of_words)
    organized_dict=alphabetize(count_diction)
    freq_list=frequency(organized_dict,number_of_words)
    out_file_name=str(input_file_name)+".out"
    out_file=open(out_file_name,"w")
    index=0
    for word,count in organized_dict.items():
        out_file.write(f'{word} {count} {freq_list[index]}\n')
        index+=1
    return input_file_name

"""Input error checking: if the format of the command line input is not in the format
'python3 freq.py 'filename'', the program states the issue and indicates the correct
format. If input is in correct format, program using write_output() to create an
output file, then outputs a statement declaring the name of created output"""
if len(sys.argv)<2:
    print(
        "Error: too few command line inputs.\n"+
        "Please type command in the following format:\n\n"+
        "python3 freq.py 'filename'\n")
    sys.exit()
elif len(sys.argv)>2:
    print(
        "Error: too many command line inputs.\n"+
        "Please type command in the following format:\n\n"+
        "python3 freq.py 'filename'\n")
    sys.exit()
else: 
    """function write_output() will return a single string with the name of the input file
    it will also create an output file with the required data. The return of a file name
    is simply to create a nicely formatted closing statement for the user."""
    filename=write_output(sys.argv[1])
    print(f"Tasks completed. Output created as {filename}.out")
