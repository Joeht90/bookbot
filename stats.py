def get_word_count(text):
    return f"Found {len(text.split())} total words"


def get_letter_count(text):
    letter_count_dict = {}
    for i in text.split():
        for j in list(i):
            if j.lower() not in letter_count_dict:
                letter_count_dict[j.lower()] = 1
                continue
            letter_count_dict[j.lower()] += 1
    return letter_count_dict


def dict_to_list(import_dict):
    list_to_be_sorted = []
    for key, value in import_dict.items():
        if key.isalpha():
            new_dict = {"char": key, "value": value}
            list_to_be_sorted.append(new_dict)
        continue
    return sorted(list_to_be_sorted, key=lambda x: x['value'], reverse=True)


def print_cleanly(list_data):
    for i in list_data:
        print(f"{i["char"]}: {i["value"]}")
