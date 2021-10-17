################################################################
#   Weekly Exercise 4: Text Preprocessor
#   CMPUT 274 Fall 2020
#
#   Ashley Davis - 1616898
################################################################

import sys

"""lowercase() will take a word and convert all capital letter in it lowercase
input values:  *word - the word in string form
return values: *word - the word in string form (now all lowercase)"""
def lowercase(word):
	word=word.lower()
	return word

"""remove_punct() will take a word and remove all symbols
input values:  *word - the word in string form
return values: *list_of_chars - the characters of the word separated in a list 
                (without punctuation or symbols)"""
def remove_punct(word):
	list_of_chars=list(word)
	charindex=0
	while charindex <len(list_of_chars):
		character=list_of_chars[charindex]
		if character.isalnum()==False:
			list_of_chars.remove(character)
		else: charindex+=1
	return list_of_chars

"""remove_numbers() will take the list of characters in the word and remove all numbers
unless all characters in the word are numbers
input values:  *list_of_chars - the characters of the word separated in a list
return values: *word - the word in string form (without numbers unless all numbers)"""
def remove_numbers(list_of_chars):
	word="".join(list_of_chars)
	if word.isnumeric()==False:
		charindex=0
		while charindex<len(list_of_chars):
			character=list_of_chars[charindex]
			if character.isnumeric():
				list_of_chars.remove(character)
			else: charindex+=1
		word="".join(list_of_chars)
	return word

"""remove_stopwords() will take a word make it an empty string if the word is a stopword
input values:  *word - the word in string form
               *stopwords - a list of stopwords
return values: *word - the word in string form or empty string if input word was a stopword"""
def remove_stopwords(stopwords,word):
	if word in stopwords:
		word=""
	return word


"""Mode assignment: takes the third command-line argument and assigns it to variable "mode",
if the command-line has only three arguments
Format: $python3 preprocess.py <mode>"""
if len(sys.argv)==2:
	mode=sys.argv[1]
	#If mode is not one of the three determined possible modes, return error message and exit
	if mode not in ["keep-symbols","keep-digits","keep-stops"]:
		print("\nERROR: MODE UNDEFINED")
		print("Please enter command-line argument in the following format:")
		print("\n         python3 preprocess.py <mode (optional)>           \n")
		print("Defined modes: keep-symbols, keep-digits, keep-stops\n")
		sys.exit()
#If the command-line has more than three arguments, return error message and exit
elif len(sys.argv)>2:
	print("\nERROR: TOO MANY COMMAND_LINE ARGUMENTS")
	print("Please enter command-line argument in the following format:")
	print("\n         python3 preprocess.py <mode (optional)>           \n")
	print("Defined modes: keep-symbols, keep-digits, keep-stops\n")
	sys.exit()
#If no mode is given, assign "mode" to have the value of "none"
else: mode="none"

#Split input line into list of separate words
line=input().split(" ")

#Create empty list to fill with processed words
processed_words=[]

#Define stopwords
stopwords=["i", "me", "my", "myself", "we", "our", 
	"ours", "ourselves", "you", "your","yours", "yourself", 
	"yourselves", "he", "him", "his", "himself", "she", 
	"her","hers", "herself", "it", "its", "itself", "they", 
	"them", "their", "theirs","themselves", "what", "which",
	"who", "whom", "this", "that", "these", "those","am", 
	"is", "are", "was", "were", "be","been", "being", "have", 
	"has", "had","having", "do", "does", "did", "doing", "a", 
	"an","the", "and", "but", "if","or", "because", "as", 
	"until", "while", "of", "at", "by", "for", "with","about", 
	"against", "between", "into", "through", "during", "before", 
	"after","above", "below", "to", "from", "up", "down", "in", 
	"out", "on", "off", "over","under", "again", "further", 
	"then", "once", "here", "there", "when", "where","why", 
	"how", "all", "any", "both", "each", "few", "more", "most", 
	"other","some", "such", "no", "nor", "not", "only", "own", 
	"same", "so", "than","too", "very", "s", "t", "can", "will", 
	"just", "don", "should", "now"]

#Process words one at a time from the list of words
for index in range(len(line)):
	word=line[index]

	#Convert letters to lowercase
	word=lowercase(word)

	#Remove punctuation unless mode=="keep-symbols"
	if mode!="keep-symbols":
		list_of_chars=remove_punct(word)
	elif mode=="keep-symbols":
		list_of_chars=list(word)

	#Remove numbers unless mode=="keep-digits"
	if mode!="keep-digits":
		word=remove_numbers(list_of_chars)
	elif mode=="keep-digits":
		word="".join(list_of_chars)

	#Remove stopwords unless mode=="keep-stops"
	if mode!="keep-stops":
		word=remove_stopwords(stopwords,word)

	#Add each word to the list of processed words unless word is an empty string
	if word!="":
		processed_words.append(word)

#Print output words
print(" ".join(processed_words))