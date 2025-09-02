def get_book_text(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
def number_of_words(book_text):
    if book_text:
        words = book_text.split()
        return len(words)
    return 0

def character_count(text: str) -> dict[str, int]:
    counts = {}
    for char in text.lower():
        if char == ' ':
            continue
        counts[char] = counts.get(char, 0) + 1
    return counts

def sort_character_count(counts: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(counts.items(), key=lambda item: item[1], reverse=True)