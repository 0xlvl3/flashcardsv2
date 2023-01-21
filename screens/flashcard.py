from test_fb import db
from datetime import datetime


class Flashcards:
    def __init__(self):
        pass

    def add_flashcards(self, deck, user_question, user_answer):
        data = {user_question: user_answer}
        current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        db.child(deck).child("flashcards").child(current_time).set(data)

    def play_deck(self, deck):
        get_cards = db.child(deck).child("flashcards").get()
        card_total = len(list(get_cards.val()))
        index = 0
        card_counter = 0

        print(card_total - 1)

        # Score counters.
        correct = 0
        incorrect = 0

        # Game loop.
        while index != card_total:
            start = list(get_cards.val().keys())[index]
            flashcards = get_cards.val()[start]

            # For the next loop.
            card_counter += 1
            index += 1

            for key, value in flashcards.items():
                print(f"{card_counter}. Question: {key}")
                user_ans = input("What is the answer? ")
                if user_ans == value:
                    print("Success")
                    correct += 1
                else:
                    print("Not correct")
                    incorrect += 1

        print(f"Correct: {correct}, incorrect: {incorrect}")

    def remove_flashcard(self, deck):

        try:
            ins = db.child(deck).child("flashcards").get()
            card_total = len(list(ins.val()))
            index = 0
            card_count = 0

            while index != card_total:
                start = list(ins.val().keys())[index]
                print(start)
                card_count += 1
                index += 1
                flashcards = ins.val()[start]
                for key in flashcards.items():
                    print(f"{card_count}. Question: {key}")
                    remove_card = input("Remove this card? (y/n): ").lower()
                    if remove_card == "y":
                        db.child(deck).child("flashcards").child(start).remove()
                    else:
                        pass

        except Exception as e:
            e = "You've entered a deck that doesn't exist"
            print(e)


# Add flashcards.
# user_input = input("What deck: ")
# flashcard.add_flashcards(user_input)

# Play flashcards.
# user_input = input("Which deck will we play? ")
# flashcard.play_deck(user_input)


# Remove a flashcard.
# user_input = input("Which deck do you want to delete cards from? ")
# flashcard.remove_flashcard(user_input)
