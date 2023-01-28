from fire_admin import db_system
from helper import update_text


class Deck:
    """
    Deck has methods create_deck, add_flashcards, delete_deck and
    inspect_deck. All methods are attached to screens within app.
    """

    def create_deck(self, uid, deck):
        """
        Function will create a deck from deck variable. Deck is stored
        within backend database.
        """
        db_system.child(uid).child(deck).set("flashcards")

    def check_for_known_deck(self, uid, deck):
        deck_check = db_system.child(uid).get()
        data = deck_check.val()
        keys = list(data.keys())
        for key in keys:
            if deck == key:
                return True
        return False

    def delete_deck(self, uid, deck):
        """
        Function will delete user specified deck.
        """
        db_system.child(uid).child(deck).remove()

    def inspect_deck(self, uid, deck):
        """
        Function will load a user specifed deck, once loaded
        user will be able to cycle through cards of specifed deck.
        """
        try:
            flashcards_indexed = []
            ins = db_system.child(uid).child(deck).child("flashcards").get()
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
            raise e


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
