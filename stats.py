def count_words(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def count_letters(text):
    text = text.lower()
    letter_count = {}
    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    return letter_count

def sort_on(items):
    return items['num']


def prettify_letter_count(letter_count):
    letter_count_list = []
    for letter,count in letter_count.items():
        letter_count_list.append({"char": letter,"num": count})
    letter_count_list.sort(reverse=True,key=sort_on)
    return letter_count_list
    
