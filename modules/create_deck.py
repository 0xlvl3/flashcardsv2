import os
from modules.utilities_funcs import write_file


def create_deck():
    """
    Function creates a directory or 'Deck' that will
    house our flashcards.json.
    """

    print("\n### Deck will be saved all lowercase")
    user_input = input(f"\nName your new deck: ").lower()

    # Check to see if directory exists.
    if not os.path.exists(user_input):
        os.mkdir(user_input)
        write_file(user_input)
    else:
        print(f"\n### {user_input} already exists! returning you to menu")
