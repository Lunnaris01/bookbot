def count_words_in_string(str):
	return len(str.split())

def count_letters_in_string_insensitive(str):
	str = str.lower()
	charset = set(str)
	return {x:str.count(x) for x in charset}

def sorted_list_of_dicts_from_dict(d):
	return sorted([{"char":x[0],"count":x[1]} for x in d.items()], key = lambda x: x["count"], reverse = True)
