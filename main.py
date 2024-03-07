def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(text)
    print(f"there are {count} words in Frankenstein")


def get_word_count(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
