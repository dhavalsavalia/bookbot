import sys

from stats import characters_frequency, get_num_words, pretty_print_char_freq


def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print(pretty_print_char_freq(characters_frequency(book_text)))
    print("============= END ===============")

main()