"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you cab generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""


# It was assumed spaces and capital letters are unique characters that need to be contained in the characters to create
# the required phrase. If not, lower() and replace(‘ ’, ‘’) can be used to remove these characters from the phrase.

def generate_phrase(characters, phrase):
    # create a dictionary and add the available chars from characters
    available_char = {}  # eg. {'c': 3, 'b': 2, 'a': 2, '@': 1, ' ': 2}
    for char in characters:
        available_char[char] = available_char.get(char, 0) + 1  # get() uses the default value for non-existent keys

    # Check if enough chars available, once the stock becomes -1, returns False
    for char in phrase:
        available_char[char] = available_char.get(char, 0) - 1
        if available_char[char] < 0:
            return False
    return True


characters1 = "cbacbac@  "
phrase1 = "@aabbccc"

characters2 = "123   456"
phrase2 = "654321123"

characters3 = ""
phrase3 = ""

print(generate_phrase(characters1, phrase1))  # True
print(generate_phrase(characters2, phrase2))  # False
print(generate_phrase(characters3, phrase3))  # True
