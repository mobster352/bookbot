# stats = name of file you want to import from
# get_number_words = name of function in that file
from stats import get_number_words, get_number_characters

# get_book_text
# Inputs: -string --path to a file
# Output: -string --contents of a file as a string
def get_book_text(filepath):
    contents = None
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_number_words(text)
    chars = get_number_characters(text)
    print(f"{num_words} words found in the document")
    for char in chars:
        print(f"'{char}': {chars[char]}")

main()