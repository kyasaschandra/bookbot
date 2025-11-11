import sys
from stats import get_num_words
from stats import count_characters

def get_book_text(path_to_file):
    print(f'Analyzing book found at {path_to_file}...')
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    args = sys.argv
    if len(args)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = args[1]
    print("============ BOOKBOT ============")
    book = get_book_text(path)
    print("----------- Word Count ----------")
    print(f'Found {get_num_words(book)} total words')
    print("--------- Character Count -------")
    count = count_characters(book)
    for i in count:
        print(f'{i}: {count[i]}')

main()
