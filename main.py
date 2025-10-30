def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())


def main():
    count = get_word_count(get_book_text("books/frankenstein.txt"))
    print(f"Found {count} total words")


main()
