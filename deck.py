from test_fb import db
from datetime import datetime


class Deck:
    def __init__(self):
        pass

    def create_deck(self, user_str, deck):
        self.user_str = user_str
        db.child(user_str).child(deck).set("flashcards")

    def add_flashcards(self):
        user_deck = input("Which deck are we placing these in: ")
        user_question = input("Question: ")
        user_answer = input("Answer: ")

        data = {user_question: user_answer}
        current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        db.child(self.user_str).child(user_deck).child("flashcards").child(
            current_time
        ).set(data)

    def delete_deck(self, deck):
        db.child(deck).remove()

    def inspect_deck(self, deck):

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


user_deck = Deck()

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
