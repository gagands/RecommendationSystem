# This file will import all data from firebase and convert to different csv
#


from google.cloud import firestore
from langdetect import detect
from langdetect import DetectorFactory
from langdetect.lang_detect_exception import  LangDetectException

DetectorFactory.seed = 0

db = firestore.Client("poetry-dev")
items_ref = db.collection(u'items')
items = items_ref.get()

result_csv_file = open("detected_languages.csv", "w")
error_csv_file = open("errors.csv", "w")
result_csv_file.write("")

for item in items:
    poem_body = item.get("body")
    body = poem_body
    # print(item.get('body'))
    # print(body[0:100])

    try:
      detected_lang = detect(body)
      result_csv_file.write(item.get("itemId"))
      result_csv_file.write(', ')
      result_csv_file.write(detected_lang)
      result_csv_file.write(', ')
      result_csv_file.write(item.get("language"))
      # result_csv_file.write(item.get('body'))
      result_csv_file.write("\n ")


    except LangDetectException as e:

      error_csv_file.write(body)
      error_csv_file.write(", ")
      # error_csv_file.write("LangDetectException" + e.message)
      error_csv_file.write("\n")

    except Exception as e:
      print(e)