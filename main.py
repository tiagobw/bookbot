from stats import count_words, count_chars


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(book_text)
    chars_dict = count_chars(book_text)
    print(f"Found {num_words} total words")
    print(chars_dict)


main()
