def count_words(book_contents):
    words_as_list = book_contents.split()
    num_words = len(words_as_list)
    return num_words 


def count_each_character(book_contents):
    lower_cased = book_contents.lower()

    character_dictionary = {}

    for each_character in lower_cased:
        if each_character in character_dictionary:
            character_dictionary[each_character] += 1
        else:
            character_dictionary[each_character] = 1
    
    return character_dictionary

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(chars_dictionary):
    sorted_list = []
    for ch in chars_dictionary:
        sorted_list.append({"char": ch, "num": chars_dictionary[ch]})
    
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
