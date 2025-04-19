from stats import get_word_count
from stats import get_character_count
from stats import make_new_list
from stats import sort_on


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    book = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book)
    book_dict = get_character_count(book)
    book_list = make_new_list(book_dict)
    book_list.sort(reverse=True, key=sort_on)
    print(f"Found {word_count} total words")
    for i in range(len(book_list)):
        print(f"{book_list[i]["character"]}: {book_list[i]["count"]}")


main()