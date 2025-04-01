from stats import count_words_in_string, count_characters_in_string,sort_characters_count,create_clean_output
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main_output(file_path):
    text = get_book_text(file_path)
    create_clean_output(text,file_path)

    

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main_output(sys.argv[1])
    
    

if __name__ == "__main__":
    main()
