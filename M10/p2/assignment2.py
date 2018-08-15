'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secret_word
the user is to guess. This starts up an interactive game of Hangman between
the user and the computer. Be sure you take advantage of the three helper functions,
is_word_guessed, get_guessed_word, and get_available_letters,
that you've defined in the previous part.
'''
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
WORD_FILE_NAME = "words.txt"
def load_words():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print("Loading word list from file...")
	# in_file: file
	in_file = open(WORD_FILE_NAME, 'r')
	# line: string
	line = in_file.readline()
	# word_list: list of strings
	word_list = line.split()
	print("  ", len(word_list), "words loaded.")
	return word_list
def is_word_guessed(secret_word, letters_guessed):
	"""guess"""
	for i in secret_word:
		if i not in letters_guessed:
			return False
	return True
def get_guessed_word(secret_word, letters_guessed):
	"""string"""
	list_1 = list(secret_word)
	length_1 = len(secret_word)
	astr = ""
	for i in range(length_1):
		count = 0
		for j in letters_guessed:
			if j == list_1[i]:
				count = 1
		if count == 1:
			astr = astr + list_1[i]
		else:
			astr = astr + '_'
	return astr
def get_available_letters(letters_guessed):
	"""dictionary"""
	import string
	x_1 = ""
	key_ = list(string.ascii_lowercase)
	value_ = key_
	dictionary_ = dict(zip(key_, value_))
	for i in letters_guessed:
		if i in dictionary_.values():
			del dictionary_[i]
	for v_1 in dictionary_.values():
		x_1 = x_1 + v_1
	return x_1		
def choose_word(word_list):
	"""string"""
	return random.choice(word_list)
WORD_LIST = load_words()
def hangman(secret_word):
	"""secret"""
	word_size = len(secret_word)
	guess_string = ""
	print("The letter contains ", word_size)
	# print('The word is ', secret_word)
	available_guess = word_size
	while available_guess > 0:
		guess_character = input("Enter a character ")
		guess_string = guess_string + guess_character
		if guess_character in secret_word:
			print("You guessed it right")
			print(get_guessed_word(secret_word, guess_string))
			print(get_available_letters(guess_string))
			if is_word_guessed(secret_word, guess_string) is True:
				print("you won")
				break
		else:
			available_guess -= 1
			print("wrong guess")
			print("number of guesses are:", available_guess)
			print(get_guessed_word(secret_word, guess_string))
			print(get_available_letters(guess_string))
	if is_word_guessed(secret_word, guess_string) is True:
		print('congratulations')
	else:
		print('The word is ', secret_word)
def main():
	'''
	Main function for the given program
	When you've completed your hangman function, uncomment these two lines
	and run this file to test! (hint: you might want to pick your own
	secret_word while you're testing)
	'''
	secret_word = choose_word(WORD_LIST).lower()
	hangman(secret_word)
if __name__ == "__main__":
	main()
