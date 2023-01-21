from test_fb import db
from datetime import datetime


class Deck:
    """
    Deck has methods create_deck, add_flashcards, delete_deck and
    inspect_deck. All methods are attached to screens within app.
    """

    def __init__(self):
        pass

    def create_deck(self, deck):
        """
        Function will create a deck from deck variable. Deck is stored
        within backend database.
        """
        db.child(deck).set("flashcards")

    def add_flashcards(self):
        """
        Function will add a flashcard to a specified deck.
        User will be prompted for question and answer, that data
        will be stored in backend database under specified deck.
        """
        user_deck = input("Which deck are we placing these in: ")
        user_question = input("Question: ")
        user_answer = input("Answer: ")

        data = {user_question: user_answer}
        current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        db.child(user_deck).child("flashcards").child(current_time).set(data)

    def delete_deck(self, deck):
        """
        Function will delete user specified deck.
        """
        db.child(deck).remove()

    def inspect_deck(self, deck):
        """
        Function will load a user specifed deck, once loaded
        user will be able to cycle through cards of specifed deck.
        """
        try:
            flashcards_indexed = []
            ins = db.child(deck).child("flashcards").get()
            card_total = len(list(ins.val()))
            index = 0
            card_count = 0

            while index != card_total:
                start = list(ins.val().keys())[index]
                card_count += 1
                index += 1
                flashcards = ins.val()[start]
                for key, value in flashcards.items():
                    flashcards_indexed.append((card_count, key, value))

            return flashcards_indexed

        except Exception as e:
            e = "You've entered a deck that doesn't exist"
            print(e)


# user_deck is used within multiple screens.
user_deck = Deck()

# Testing.
# -------

# deck = Deck()

# Create a deck.
# deck.create_deck()

# Add flashcards + create a deck.
# deck.add_flashcards()

# Remove a deck.
# user_input = input("Remove what deck: ")
# deck.delete_deck(user_input)

# Inspect deck.
# user_input = input("What deck will you view: ")
# inspect_deck(user_input)
# print(flashcards_indexed[0][2])
