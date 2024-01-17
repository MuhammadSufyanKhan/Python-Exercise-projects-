def number_to_words(number):
    """Convert a number to its word equivalent for the 'Ten Green Bottles' song.

    :param number: int - the number to convert.
    :return: str - the word equivalent.
    """
    number_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
    return number_words[number]


def recite(start, take=1):
    """Recite the lyrics of the 'Ten Green Bottles' song.

    :param start: int - starting number of green bottles.
    :param take: int - optional parameter specifying how many verses to recite.
    :return: None
    """
    
    for i in range(start, start - take, -1):
        current_bottles = number_to_words(i)
        next_bottles = number_to_words(i - 1) if i - 1 >= 0 else "no"
        print(f"{current_bottles} green bottle{'s' if i > 1 else ''} hanging on the wall,")
        print(f"{current_bottles} green bottle{'s' if i > 1 else ''} hanging on the wall,")
        print("And if one green bottle should accidentally fall,")
        print(f"There'll be {next_bottles.lower()} green bottle{'s' if i-1 != 1 else ''} hanging on the wall.\n")

# Example usage:
recite(10, 10)
