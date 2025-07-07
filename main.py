from stats import count_words, count_letters, prettify_letter_count
import sys

def get_book_text(file_path):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        file_path (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def print_report(letter_list,word_count ,file_path):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for letter in letter_list:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")
    print(f"============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    file_path = sys.argv[1]
    contents = get_book_text(file_path)
    letter_list = prettify_letter_count(count_letters(contents))
    word_count = count_words(contents)
    print_report(letter_list,word_count,file_path)
    #print(f"{count_words(contents)} words found in the document.")


main()

