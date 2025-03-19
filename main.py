

def get_book_text(file_path):
    book_text = ""
    with open(file_path) as f:
        book_text += f.read()
    return book_text

def main():
    print(get_book_text("books/frankenstein.txt"))

main()