import sys
from stats import *

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = get_word_count(book_text)
    num_chars = get_char_count(book_text)
    sorted_char_count = sort_char_count(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for line in sorted_char_count:
        if line["character"].isalpha():
            print(f"{line['character']}: {line['count']}")
    print("============= END ===============")
    
main()