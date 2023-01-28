from fire_admin import db_system
from datetime import datetime


class Flashcards:
    """
    Flashcards class stores methods related to flashcards.
    Such as add_flashcards, play_deck and remove_flashcard.
    """

    def __init__(self):
        pass

    def add_flashcards(self, deck, user_question, user_answer, user_code):
        """
        Function will add a flashcard to a user specified deck.
        Flashcard will take question and answer as data.
        """
        data = {user_question: user_answer}
        current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        db_system.child(user_code).child(deck).child("flashcards").child(
            current_time
        ).set(data)

    def play_deck(self, deck):
        """
        Function will load a user specified deck then prompt the user with
        a question it wil then wait for user input of answer to see if it matches
        with answer stored to the card.
        """
        get_cards = db_system.child(deck).child("flashcards").get()
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
        """
        Function will remove a specified flashcard from a specified user deck.
        """

        try:
            ins = db_system.child(deck).child("flashcards").get()
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
                        db_system.child(deck).child("flashcards").child(start).remove()
                    else:
                        pass

        except Exception as e:
            e = "You've entered a deck that doesn't exist"
            print(e)

        # Question check for dub questions.
        def check_for_exisiting_question(self, uid, deck, question):

            deck_check = db_system.child(uid).child(deck).child("flashcards").get()
            data = deck_check.val()
            if data is None:
                pass
            else:
                pair = list(data.items())
                for key, value in pair:
                    for k, v in value.items():
                        if question == k:
                            return True
                    return False


user_flashcards = Flashcards()
