def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(book):
    book_list = book.split()
    return len(book_list)

def main():
   book = get_book_text("books/frankenstein.txt")
   print(f"{get_word_count(book)} words found in the document")
main()