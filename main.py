


import sys
from stats import character_count, get_book_text, number_of_words, sort_character_count


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    book_text = get_book_text(book_path)
    print("Found", number_of_words(book_text), "total words")
    print("--------- Character Count -------")
    char_counts = character_count(book_text)
    sorted_counts = sort_character_count(char_counts)
    for char, count in sorted_counts:
        print(f"{char}: {count}")


if __name__ == "__main__":
    main()