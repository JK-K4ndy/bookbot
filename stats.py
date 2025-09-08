def get_word_count(text):
    words = text.split()
    return(len(words))

def get_char_appearance(text):
    chars = {}
    for c in text:
        if c.lower() not in chars:
            chars[c.lower()] = 0
        chars[c.lower()] += 1
    return chars

def sorted_dict_list(dict):
    dict_list = []
    for char in dict:
        if char.isalpha():
            dict_list.append({"c": char, "n": dict[char]})
    dict_list.sort(reverse=True, key=lambda items: items["n"])
    return dict_list

def book_report(book_src, words, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_src}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for d in char_list:
        print(f"{d["c"]}: {d["n"]}")
    print("============= END ===============")