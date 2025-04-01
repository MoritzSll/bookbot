def count_words_in_string(string):
    word_list = string.split()
    return len(word_list)

def count_caracters_in_string(string):
    lowercase_string = string.lower()
    character_dict = {}
    for c in lowercase_string:
        if c in character_dict:
            character_dict[c] += 1
        else:
            character_dict[c] = 1
    return character_dict




