def get_word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    book_list = f.split()
    return len(book_list)


def get_character_count(filepath):
    # Create blank dictionary
    character_counts = {}
    # With block to open file
    with open(filepath) as f:
        # create a variable of the file as a string
        file_contents = f.read()
        # For loop to iterate through each string index
    for i in file_contents:
        # Increment dictionary for each string and make sure to 
        # .lower() the iteration to avoid duplicates
        # Had to add an if statement was unable to create a new key value
        # while incrementing
        if i.lower() in character_counts:
            character_counts[i.lower()] += 1
        else:
            character_counts[i.lower()] = 1
    return character_counts


