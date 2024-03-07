def main():
    book_path = "books/Frankenstein.txt"
    text = get_book_text(book_path)
    print_report(text, book_path)

def print_report(text, path):
    word_count = get_word_count(text)
    letter_count = sort_dict(get_letter_count(text))
    
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for l in letter_count:
        print(f"The '{l["letter"]}' character was found {l["count"]} times")
    print("--- End report ---")
    


def sort_dict(dict):
    sorted_dict = []
    for d in dict:
        sorted_dict.append({"letter": d, "count":dict[d]})
    def sort_on(dict):
        return dict["count"]
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict



def get_letter_count(text):
    letter_dict = {}
    lowered_text = text.lower()
    for i in range(len(lowered_text)):
        if lowered_text[i].isalpha() == False:
            continue
        elif lowered_text[i] not in letter_dict:
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
