# Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate("files/key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def create():

    user_collection = input("What do you want to name your deck? ")
    collection_ref = db.collection(f"{user_collection}").document()
    question = input("question: ")
    answer = input("answer: ")
    flashcard = {question: answer}


test_ref = db.collection("Test").stream()
get_bal = test_ref.get({"Balance"})
bal = "{}".format(get_bal.to_dict())
print(bal)
for doc in test_ref:

    test = "{}".format(doc.to_dict())

    print(f"{doc.id} => {doc.to_dict()}")

# cards_ref = db.collection(f"{user_collection}")
# docs = cards_ref.stream()
# counter = 0
# for doc in docs:
#    counter += 2
#    print(f"{counter}. {doc.to_dict()}")


# obj1 = {"Name": "Mike", "Age": 100, "Net": 1000000}
# obj2 = {"Name": "Tony", "Age": 200, "Net": 200}

# data = [obj1, obj2]

# for record in data:
#    print(record)
#    doc_ref = db.collection("Users").document(record["Name"])
#    doc_ref.set(record)

# users_ref = db.collection("Users")
# docs = users_ref.stream()

# for doc in docs:
#    if doc.id == "Mike":
#        print("Mike exists")
#    else:
#        print(f"{doc.id} => {doc.to_dict()}")
