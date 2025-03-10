import sys
from stats import count_words_in_string, count_letters_in_string_insensitive,sorted_list_of_dicts_from_dict

def get_book_text(path):
	with open(path) as f:
		book_content = f.read()
		return book_content



def main():
	if len(sys.argv)<2:
		print("Missing Path to book")
		return
	book_content = get_book_text(sys.argv[1])
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {count_words_in_string(book_content)} total words")
	print("--------- Character Count -------")
	letters_d = count_letters_in_string_insensitive(book_content)
	sorted_d = sorted_list_of_dicts_from_dict(letters_d)
	for entry in sorted_d:
		if entry["char"].isalpha():
			print(f"{entry["char"]}: {entry["count"]}")
if __name__ == '__main__':
	main()
