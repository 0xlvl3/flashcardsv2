import os
import json
import shutil

flashcards = {}


def check_if_flashcard_exists(question, answer, json_data):
    """
    Function checks if flashcard is already apart of user specified deck.
    """

    if question in json_data and json_data[question] == answer:
        return True
    return False


def user_choice_deck(deck, question, answer):
    """
    Function takes user choice to create a new deck
    while in add_flashcard function; this function will
    create the deck and also put flashcard in that deck.
    """

    user_choice = input(
        f"\n{deck} doesn't exist do you want to create it? Y/N:  "
    ).lower()

    if user_choice.lower() == "y":
        os.mkdir(deck)
        print(f"\n{deck} has been created! flashcard {question} has been added too!")
        with open(f"{deck}/flashcard.json", "w") as cards:
            flashcards = {question: answer}
            json.dump(flashcards, cards, indent=4)

    else:
        print("Returning to menu")


def create_deck():
    """
    Function creates a directory or 'Deck' that will
    house our flashcards.json.
    """

    print("\n### Deck will be saved all lowercase")
    userInput = input(f"\nName your new deck: ").lower()

    # Check to see if directory exists.
    if not os.path.exists(userInput):
        os.mkdir(userInput)
        with open(f"{userInput}/flashcard.json", "w") as cards:
            flashcards = {}
            json.dump(flashcards, cards)
            print(f"\n{userInput} has been created, go add flashcards!")

    else:
        print(f"\n### {userInput} already exists! returning you to menu")


def add_flashcard():
    """
    Function will add a 'question' + 'answer' into a json
    within a specified directory; won't add dupe flashcards.
    """
    # Ask the user for the flashcard question and answer.
    question = input("\nEnter the flashcard question: ").lower()
    answer = input("Enter the flashcard answer: ").lower()

    user_named_deck = input("Name of the deck you wish to add this card: ").lower()

    # Check if directory exists.
    if os.path.isdir(user_named_deck):
        with open(f"{user_named_deck}/flashcard.json", "r") as cards:
            flashcards = json.load(cards)

            # Checks if card is a duplicate.
            if check_if_flashcard_exists(question, answer, flashcards):
                print(
                    f"""
\n### The "{question}" flashcard in {user_named_deck} already exists!
Returning to menu                     
                    """
                )

            # Add the flashcard to the dictionary.
            else:
                flashcards[question] = answer
                print(f'\n### "{question}" card has been added to {user_named_deck}')
                with open(f"{user_named_deck}/flashcard.json", "w") as cards:
                    json.dump(flashcards, cards, indent=4)

    # If directory doesn't exists; Will create and add card to that directory.
    else:
        user_choice_deck(user_named_deck, question, answer)


def play_cards():
    """
    Function will play through flashcards; user will be
    asked a question and prompted for an answer until deck
    has no cards left.
    """
    deck_choice = input("Which deck do you want to run through? ").lower()

    # If directory exists game starts.
    if os.path.exists(deck_choice):
        with open(f"{deck_choice}/flashcard.json", "r") as f:
            data = json.load(f)

            # Game counters.
            card_count = 0
            correct = 0
            incorrect = 0

            # Card loop.
            for question, answer in data.items():
                card_count += 1
                print(f"\n{card_count}. {question}")
                user_answer = input("Type answer here: ").lower()
                if user_answer == answer:
                    correct += 1
                else:
                    incorrect += 1

        # Play score.
        print(
            f"""
(ﾉ◕ヮ◕)ﾉ*:・ﾟ✧・ﾟ✧
Out of {card_count} you got {correct} correct and {incorrect} incorrect
                        """
        )

    # If directory doesn't exist return to menu.
    else:
        print(f"\n### {deck_choice} deck does not exist returning to menu")


def inspect_deck():
    """
    Function will return a list of cards within a specified deck.
    """
    deck_choice = input("Name of the deck you wish to inspect: ").lower()

    # If deck exists.
    if os.path.exists(deck_choice):
        json_file = None
        for flashcards in os.listdir(deck_choice):
            if flashcards.endswith(".json"):
                json_file = flashcards
            print(f"\nThese are the current flashcards in {deck_choice}")
            with open(os.path.join(deck_choice, json_file)) as card_list:
                data = json.load(card_list)
                counter = 1
                for question, answer in data.items():
                    print(
                        f"""
            +---------------------------------------
          {counter}.| Question: {question}
            | Answer: {answer}
                        """
                    )
                    counter += 1

            print("\nDeck list finished! go add more")
    # If deck doesn't exist.
    else:
        user_answer = input(
            f"\n{deck_choice} doesn't exist do you want to create it? Y/N:  "
        ).lower()
        if user_answer.lower() == "y":
            os.mkdir(deck_choice)
            with open(f"{deck_choice}/flashcard.json", "w") as cards:
                flashcards = {}
                json.dump(flashcards, cards)
                print(f"\n### {deck_choice} has been created, go add flashcards!")
        else:
            print("\n### Returning to menu")


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


def open_menu(menu_txt):
    with open(menu_txt, "r") as menu:
        menu_read = menu.read()
    print(menu_read)


def close_menu(menu_txt):
    menu_txt.close()


open_menu("menu.txt")


def main():
    """
    Main loop for our flashcards program
    """

    while True:
        print("\n'ls' to see the menu again")
        action = input("choose an action: ").lower()

        if action == "c":
            create_deck()
        elif action == "a":
            add_flashcard()
        elif action == "p":
            play_cards()
        elif action == "i":
            inspect_deck()
        elif action == "d":
            delete_deck()
        elif action == "ls":
            open_menu("menu.txt")
        elif action == "e":
            exit()


main()
