def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        wordcounter = word_count(file_contents)
        charcounter = char_count(file_contents)
        print(f"--- Begin report of {path_to_file} ---")
        print(f"{wordcounter} words found in the document")
        for i in charcounter:
            if i.isalpha():
                print(f'The \'{i}\' character was found {charcounter[i]} times')

def word_count(s:str) -> int:
    return len(s.split())

def char_count(s:str)-> dict[str,int]:
    charcount_dict = {}
    for c in s.lower():
        if charcount_dict.get(c):
            charcount_dict[c] +=1
        else:
            charcount_dict[c] = 1
    return charcount_dict


main("books/frankenstein.txt")