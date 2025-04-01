from stats import count_words_in_string, count_characters_in_string,sort_characters_count,create_clean_output

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    text = get_book_text("books/frankenstein.txt")
    create_clean_output(text)

if __name__ == "__main__":
    main()
