def get_word_count(text):
    return len(text.split())


def get_letter_count(text):
    letter_count_dict = {}
    for i in text.split():
        for j in list(i):
            if j.lower() not in letter_count_dict:
                letter_count_dict[j.lower()] = 1
                continue
            letter_count_dict[j.lower()] += 1
    return letter_count_dict


def sort_dict_to_list(dict):
    list_to_be_sorted = []
    for key, value in dict:
        list_to_be_sorted += {"char": key, "num": value}
    return sorted(list_to_be_sorted, key=lambda x: x['num'])

