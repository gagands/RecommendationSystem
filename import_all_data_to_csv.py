from google.cloud import firestore
db = firestore.Client("poetry-dev")
items_ref = db.collection(u'items')
items = items_ref.get()
poem_no = 0
language_set = 0
language_not_set = 0

for item in items:

    poem_num = poem_num + 1
    item_language = item.get("language")
    if (item_language == "unknown_XX") or (item_language == "not supported"):
        language_not_set = language_not_set + 1
    else :
        language_set = language_set + 1

print(str(language_not_set) + ' poems do not have language set.')
print(str(language_set) + ' poems have language set.')
print(str(poem_num) + " poems are there in total")

print(str((language_not_set * 1.0) / poem_num * 100) + "% poems don't have language set.")





