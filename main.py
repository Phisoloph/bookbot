def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    num_words = get_num_words(text)
    print(num_words)
    num_chars = get_char_dict(text)
    print(num_chars)
    num_chars = convert_dict(num_chars)
    num_chars.sort(reverse=True, key=sort_on)
    print(num_chars)
    result_string = report(book_path, num_words, num_chars)
    print(result_string)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(string):
    words = string.split()
    return len(words)

def get_char_dict(string):
    chars = {}
    for c in string:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def convert_dict(dict):
    list_of_dicts = [{'character': char, 'count': count} for char, count in dict.items() ]
    return list_of_dicts

def sort_on(dict):
    return dict["count"]

def report(book_path, num_words, num_char):
    result_string = ""
    result_string += "--- Begin report of " + book_path + " ---\n"
    result_string += str(num_words) + " words found in the document\n\n"
    for item in num_char:
        if item['character'].isalpha():
            result_string += f"The '{item['character']}' character was found {item['count']} times.\n"
    result_string += "--- End report ---"
    return result_string

if __name__ == '__main__':
    main()