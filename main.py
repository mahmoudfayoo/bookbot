def get_book_text(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    if book_text:
        print(book_text)

if __name__ == "__main__":
    main()