from collections import *
import time

dictionary_file = open("english.txt", "r")
#dictionary = set()
dictionary = []
for word in dictionary_file:
	if (len(word.strip())) >= 3:
		#dictionary.add(word.strip().lower())
		dictionary.append(word.strip().lower())

def validate_prefix(prefix):
	#return any(word.startswith(prefix) for word in dictionary)
	for word in dictionary:
		if word.startswith(prefix):
			return True
	return False

def validate_word(test_word):
	return test_word in dictionary

def string_to_dictionary(input_string):
	letter_count = Counter()

	for letter in input_string:
		letter_count[letter] += 1

	return letter_count

def next_letter(input_string,letter_count):
	valid_letters = []
	#return if there are no letters left
	if not letter_count:
		return valid_letters

	letters = letter_count.keys()
	
	for letter in letters:
		prefix = input_string + letter
		if validate_prefix(prefix):
			valid_letters.append(letter)
	return valid_letters

	# prefixes = []
	# for letter in letters:
	# 	prefixes.append(input_string+letter)

	# prefixes_tuple = tuple(prefixes)

	# words = [word for word in dictionary if word.startswith(prefixes_tuple)]

def use_letter(letter_count,letter):
	letter_count[letter] -= 1
	letter_count += Counter()

def find_anagram(input_string,letter_count):
	is_word = validate_word(input_string)
	next_letters = next_letter(input_string,letter_count)
	# base case - no more letters left
	if len(next_letters) == 0:
		if is_word:
			return [input_string]
		else:
			return []
	# recursive case - keep going (but add your current word if it is a word)
	else:
		all_words = []
		if is_word:
			all_words.append(input_string)
		for letter in next_letters:
			letter_count_used = Counter(letter_count)
			use_letter(letter_count_used,letter)
			return_value = find_anagram(input_string + letter,letter_count_used)
			if return_value != []:
				all_words.append(return_value)
		return all_words

def generate_dictionary2(input_string):
	letters = string_to_dictionary(input_string)
	prefixes = []
	global dictionary

	for letter1 in letters.keys():
		for letter2 in letters.keys():
			for letter3 in letters.keys():
				prefixes.append(letter1+letter2+letter3)

	words = []
	for prefix in prefixes:
		for word in dictionary:
			if word.startswith(prefix):
				words.append(word)


	dictionary = words

def generate_dictionary3(input_string):
	letters = string_to_dictionary(input_string)
	prefixes = []
	global dictionary

	for letter1 in letters.keys():
		for letter2 in letters.keys():
			for letter3 in letters.keys():
				prefixes.append(letter1+letter2+letter3)

	words = []

	prefixes_tuple = tuple(prefixes)

	for word in dictionary:
		if word.startswith(prefixes_tuple):
			words.append(word)

	dictionary = words

def generate_dictionary(input_string):
	letters = string_to_dictionary(input_string)
	prefixes = []
	global dictionary

	for letter1 in letters.keys():
		for letter2 in letters.keys():
			for letter3 in letters.keys():
				prefixes.append(letter1+letter2+letter3)

	prefixes_tuple = tuple(prefixes)

	#words = {word for word in dictionary if word.startswith(prefixes_tuple)}
	words = [word for word in dictionary if word.startswith(prefixes_tuple)]

	dictionary = words
	print (len(dictionary))

def solve_anagram(input_string):
	generate_dictionary(input_string)
	letters = string_to_dictionary(input_string)
	return find_anagram('',letters)

if __name__ == "__main__":
	start = time.time()
	#kevin = string_to_dictionary('kevinngo')

	#print(find_anagram('',ngo))
	print(type(dictionary))
	print(solve_anagram('ecebkasdfasdhnhko'))
	
	# print (len(dictionary))


	# generate_dictionary3('ecebkasdfasdhnhkooirtyweqd')
	# print (len(dictionary))


	print(type(dictionary))
	end = time.time()
	print(end - start)