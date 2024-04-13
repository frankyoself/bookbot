

def main():
    # get book text"
    print ("type the book name:")
    try:

        book_path = "books/" + input() + ".txt"
    except EOFError:
        print (f"please enter a book name")
    except FileNotFoundError:
        print (f"this filename is not found: {book_path}")

    # book_path = "/home/residentia/workspace/text.txt"

    text = get_book_text(book_path)
    # get number of words, print out
    word_count = get_word_count(text)
    print (f"{word_count} words found in \n{book_path}")

    low_text = text.lower()
    letter_dict = get_letter_dict_list(low_text)
    

    print_dict_report (letter_dict, book_path, word_count)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def get_word_count(text):
    return len(text.split())


def get_letter_list(letter_list): 
    # take a character list and make it an alphabetical list
    letter_list_from = "".join(letter_list)
    alpha_list = []

    for c in letter_list_from:
        # print (f"c = {c}")
        if c.isalpha():
            alpha_list.append(c)
            # print (f"letter_list appended: \n{alpha_list}")
    
    # print (f"letter list: {alpha_list}")
    return alpha_list   

def get_letter_dict_list (text):
    letter_dict = []
    word_list = text.split()
    letter_list = get_letter_list("".join(word_list))
    # print (f"word list: {word_list}")
    # print (f"letter list: {letter_list}")
    letter_set = set(letter_list)
    # print (f"here are all unique letters: {letter_set}")
    i = 0
    for c in letter_set:
        counter = 0
        # print (f"c = {c}")
        for ch in letter_list:
            if c == ch:
                counter += 1
                # print (f"counter updated = {counter}")
        letter_dict.append({"key": c, "value": counter})
        i += 1
        # print (f"letter dict updated \n{letter_dict}")


    return letter_dict


def print_dict_report (dict_list, path, word_count):

    print (f"--- Begin report of {path} ---")
    print (f"{word_count} words found in the document")

    # dict_list = make_dict_list(dict)
    dict_list.sort(reverse=True, key=sort_on)
    # print (dict_list)
    sz = len(dict_list)
    for i in range (sz):
        print (f"The {dict_list[i]["key"]} character was found {dict_list[i]["value"]} times")

def sort_on (dict, key="value"):
    return dict[key]
"""""
def make_dict_list(dict):
    # take a large dictionary of keys and values, and make a list of paired dictionaries
    key_list = list(dict.keys())
    value_list = list(dict.values())
    # print (f"key_list, value_list: {key_list} \n{value_list}")
    new_dict = [
        {"key": "", "value": int()}
    ]
    sz = len (key_list)
    new_dict.pop()
    for i in range (sz):
        new_item = {"key": key_list[i], "value": value_list[i]}
        new_dict.append( new_item )

    return new_dict
"""

main()
