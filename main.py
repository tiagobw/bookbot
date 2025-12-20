import sys
from stats import count_words, count_chars, generate_sort_chars, print_sorted_chars


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if (len(sys.argv)) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(f"./{book_path}")
    num_words = count_words(book_text)
    chars_dict = count_chars(book_text)
    sorted_chars = generate_sort_chars(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_sorted_chars(sorted_chars)
    print("============= END ===============")


main()
