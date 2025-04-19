def get_word_count(book):
    book_list = book.split()
    return len(book_list)


def get_character_count(book):
    # Create blank dictionary
    character_counts = {}
        # For loop to iterate through each string index
    for i in book:
        # Increment dictionary for each string and make sure to 
        # .lower() the iteration to avoid duplicates
        # Had to add an if statement was unable to create a new key value
        # while incrementing
        if i.isalpha():
            if i.lower() in character_counts:
                character_counts[i.lower()] += 1
            else:
                character_counts[i.lower()] = 1
    return character_counts


def sort_on(dict):
    return dict["count"]


def make_new_list(dict):
    new_list = []
    for i in dict:
        new_list.append({"character": i, "count": dict[i]})
    return new_list

