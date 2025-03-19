def word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def get_book_text(file_path):
    book_text = ""
    with open(file_path) as f:
        book_text += f.read()
    return book_text