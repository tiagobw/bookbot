from stats import count_words, count_chars, generate_sort_chars, print_sorted_chars


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(book_text)
    chars_dict = count_chars(book_text)
    sorted_chars = generate_sort_chars(chars_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_sorted_chars(sorted_chars)
    print("============= END ===============")


main()
