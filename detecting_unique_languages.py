# detects no. of poems of user's choice from detected_languages.csv
# add _CountryCode in the end of language
#

import pandas as pd

col_names = ['poemId', 'detected_lang', 'user_lang']
df = pd.read_csv("detected_languages.csv", sep=', ', header=None, names=col_names)

# df = df.groupby('detected_lang').nunique()
# print (df)


en_only = df[df.detected_lang == 'hi']         # enter language to be detected in ''
en_only['detected_lang'] = en_only['detected_lang'].astype(str) + '_IN'   # for adding _CountryCode with 'language'

en_only.to_csv(r'hindi_poems.csv')      # create the csv named 'language'_poems.csv
print (df['detected_lang'].unique())
print (en_only)