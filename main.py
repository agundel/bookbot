def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
#    count = get_word_count(text)
#    print(f"there are {count} words in Frankenstein")
    letters = count_letters(text)
    print(letters)

def count_letters(text):
    letter_dict = {}
    lowered_text = text.lower()
    for i in range(len(lowered_text)):
        if lowered_text[i] not in letter_dict:
            letter_dict[lowered_text[i]] = 1
        else:
            letter_dict[lowered_text[i]] += 1
    return letter_dict

def get_word_count(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
