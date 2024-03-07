def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    print(f"there are {word_count} words in Frankenstein")
#    print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
