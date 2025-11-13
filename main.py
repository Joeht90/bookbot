from stats import get_word_count, get_letter_count, dict_to_list, print_cleanly
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text_from_book = get_book_text(sys.argv[1])
    count = get_word_count(text_from_book)
    letter_count = get_letter_count(text_from_book)
    sorted_list = dict_to_list(letter_count)
    print(f"============ BOOKBOT ============\n"
    "Analyzing book found at {sys.argv[1]}...\n"
    "----------- Word Count ----------\n"
    "{get_word_count(text_from_book)}\n"
    "--------- Character Count -------")
    print_cleanly(sorted_list)


main()
