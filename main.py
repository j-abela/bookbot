from stats import *

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = word_count(book_text)
    num_chars = count_chars(book_text)
    print(f"{num_words} words found in the document") 
    print(num_chars)                  

main()