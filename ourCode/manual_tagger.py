"""
The purpose of this script is to speed the process of manually tagging words as
positive or negative.
"""

from sentimentAnalysis import sentiment_Analysis
import pandas as pd
import enchant
import sys

# gather tweets and scrape
ss = sentiment_Analysis()
dic = ss.get_data(count=5, query='collectData', fileName='../data/political_names.csv')
dic = ss.scrape_tweet(tweetDict=dic)

# get words that indicate sentiment
bow = ss.get_sentimental_words(dic)

# only allow valid English words
spellcheck = enchant.Dict("en_US")
bow = [x for x in bow if spellcheck.check(x)]
print(len(bow))
# create dataframe for the tagging
df = pd.DataFrame(bow)
df.columns = ['word']
df['sentiment'] = ''

for index, row in df.iterrows():
    valid = False
    while not valid:
        # capture keyboard input, ctrl+D to save progess
        try:
            res = input('Word: '+row['word']+ '\tsentiment val: ')
        except EOFError:
            df.to_csv('tagged.csv', encoding='utf-8')
            sys.exit(0)

        # only accept integer inputs
        try:
            res = int(res)
        except:
            pass

        # 1 = negative, 2 = neutral, 3 = positive
        if res == 1 or res == 2 or res == 3:
            valid = True
            val = 'neut'
            if res == 1:
                val = 'neg'
            elif res == 3:
                val = 'pos'
            row['sentiment'] = val


# saved tagged data
df.to_csv('small_tagged.csv', encoding='utf-8')
