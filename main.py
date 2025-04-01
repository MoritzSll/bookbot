from stats import count_words_in_string

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    print(count_words_in_string(get_book_text("books/frankenstein.txt")), "words found in the document")

if __name__ == "__main__":
    main()
