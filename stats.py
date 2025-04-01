def count_words_in_string(string):
    word_list = string.split()
    return len(word_list)

def count_characters_in_string(string):
    lowercase_string = string.lower()
    character_dict = {}
    for c in lowercase_string:
        if not c.isalpha():
            continue
        if c in character_dict:
            character_dict[c] += 1
        else:
            character_dict[c] = 1
    return character_dict

def sort_characters_count(c_dict):
    sorted_items = sorted(c_dict.items(), key = lambda item: item[1], reverse = True)
    sorted_dict = dict(sorted_items)
    return sorted_dict

def create_clean_output(string):
    
    c_dict = count_characters_in_string(string)
    sorted_dict = sort_characters_count(c_dict)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", count_words_in_string(string), "total words")
    print("--------- Character Count -------")

    for c in sorted_dict:
        print(c + ":",sorted_dict[c])

    print("============= END ===============")


