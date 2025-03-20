import sys
from stats import count_text
from stats import count_characters
from stats import sort_character_counts

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    return_book = get_book_text(book_path)
    num_words = count_text(return_book)
    num_char = count_characters(return_book)
    sorted_char_count = sort_character_counts(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_count:
        print(f"{entry['char']}: {entry['count']}")
    print("============= END ===============")

main()