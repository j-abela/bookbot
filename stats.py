def word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def get_book_text(file_path):
    book_text = ""
    with open(file_path) as f:
        book_text += f.read()
    return book_text

def count_chars(book_text):
    char_list = []
    char_count = {}
    for char in book_text:
        char = char.lower()
        char_list.append(char)

    for char in char_list:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] +=1
    
    return char_count
