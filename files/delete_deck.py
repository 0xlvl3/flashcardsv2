import os
import shutil


def delete_deck():
    """
    Will delete a specified directory 'deck' and all
    contents within it.
    """
    # Warn user.
    print("\nBefore you proceed this will delete all flashcards in the deck as well")
    user_ack = input("Do you wish to proceed Y/N : ").lower()
    # Delete deck
    if user_ack == "y":
        remove_deck = input("\nType the name of the deck you wish to delete: ").lower()
        if os.path.exists(remove_deck):
            shutil.rmtree(remove_deck)
            print(f"\n{remove_deck} has been removed!")
        else:
            print(f"\n### {remove_deck} is not a deck! returning to menu")

    # Return to menu.
    else:
        print("\n### Returning to the menu!")
