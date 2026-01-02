import sys

from stats import count_frequency, count_words, sort_dictionary


def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents


def print_report(path, num_words, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in char_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")


def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        text = get_book_text(path)
        num_words = count_words(text)
        freq_map = count_frequency(text)
        sorted = sort_dictionary(freq_map)
        print_report(path, num_words, sorted)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


if __name__ == "__main__":
    # This code runs only when the file is executed as a script
    main()
