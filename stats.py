def count_words(text):
    """Returns the number of words in a give string"""
    return len(text.split())


def count_frequency(text):
    """Returns the freqency map of characters in a give string"""
    frequency_map = {}
    for char in text.lower():
        if char in frequency_map:
            frequency_map[char] = frequency_map[char] + 1
        else:
            frequency_map[char] = 1

    return frequency_map


def sort_on(items):
    return items["num"]


def sort_dictionary(dict):
    """takes the dictionary of characters and their counts and returns a sorted list of dictionaries"""
    characters = []
    for key, value in dict.items():
        characters.append({"char": key, "num": value})

    characters.sort(reverse=True, key=sort_on)

    return characters
