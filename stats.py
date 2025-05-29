# get_number_words
# Inputs: -string --contents of the book
# Outputs: -int --number of words in book
def get_number_words(text):
    num_words = 0
    for word in text.split():
        num_words += 1
    return num_words

# get_number_characters
# Inputs: -string --contents of book
# Outputs: -dictionary --dictionary of each character and how many times the character is found ex. {'p': 6121, 'r': 20818, ...}
def get_number_characters(text):
    chars = {}
    for word in text.split():
        for char in word:
            lower_char = char.lower()
            if lower_char in chars:
                chars[lower_char] += 1
            else:
                chars[lower_char] = 1
    return chars

# sort_character_dictionary
# Inputs: -dictionary --character dictionary
# Outputs: -list --sorted list of character dictionary
def sort_character_dictionary(chars):
    sorted_chars = []
    for char in chars:
        sorted_chars.append({"char": char, "num": chars[char]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars

# sort_on
# Inputs: -dictionary
# Outputs: -dictionary --sorted by num
def sort_on(dict):
    return dict["num"]