from stats import *

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    num_words = get_word_count(book_text)
    num_chars = get_char_count(book_text)
    sorted_char_count = sort_char_count(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for line in sorted_char_count:
        if line["character"].isalpha():
            print(f"{line['character']}: {line['count']}")
    print("============= END ===============")
    
main()