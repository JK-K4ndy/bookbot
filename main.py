from stats import *
import sys

def get_book_text(pathtofile):
    with open(pathtofile) as f:
        return f.read()

def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_src = sys.argv[1]
    text = get_book_text(book_src)
    words = get_word_count(text)
    chars = get_char_appearance(text)
    chars_list = sorted_dict_list(chars)
    book_report(book_src, words, chars_list)
    
main()