from stats import get_word_count, get_letter_count, sort_dict_to_list


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    text_from_book = get_book_text("books/frankenstein.txt")
    count = get_word_count(text_from_book)
    print(f"Found {count} total words")
    letter_count = get_letter_count(text_from_book)
    print(sort_dict_to_list(letter_count))


main()
