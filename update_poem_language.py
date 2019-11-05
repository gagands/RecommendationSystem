# This file is for testing code before implementing on large scale
from google.cloud import firestore
import pandas as pd

db = firestore.Client("poetry-dev")
items_ref = db.collection(u'items')
items = items_ref.get()


# for testing by updating single poems
def batch_update_single_poem():
    batch = db.batch()
    poem_id = '-KSiT_YxIuwCU7bE4ZQN'
    candidate_poem_ref = items_ref.document(poem_id)
    lang = unicode('en_US')
    batch.update(candidate_poem_ref, {u"language": lang})
    batch.commit()


# for updating the whole lot

# df = pd.read_csv('hindi_poems.csv')   # change the file to language you want to update
# sliced_df = df.loc[6500:6999]             # only 500 commits in one go
# print (sliced_df)

# def batch_update_en_US():
#     batch = db.batch()
#     for i in sliced_df.index:
#         poem_id = sliced_df['poemId'][i]
#         candidate_poem = items_ref.document(poem_id)
#         lang = unicode(sliced_df['detected_lang'][i])      #unicode prevents 'lang_country' from turning to blog object
#         print (poem_id, lang)
#         batch.update(candidate_poem, {u"language": lang})
#
#     batch.commit()


# batch_update_en_US()
batch_update_single_poem()
