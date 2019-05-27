# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:04:01 2019

@authors:
    Amr Elfiky
    Tianyi Lu
    Yuesong Shi
    Edward Zamora

"""

import tweepy
from tweepy import OAuthHandler
import sys
import pickle
import os
import csv
import string
import nltk
import re
import emoji
from nltk.tokenize import regexp_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class sentiment_Analysis(object):
    '''
    Our main class for twitter interface and sentiment analysis
    '''
    def __init__(self):
        '''
        Construction and initilization
        '''
        #Setup Twitter authentication variables
        # Don't have these values yet
        consumer_key = 'sy03DqAPbKjcAHG1yE2aXrM0j'
        consumer_secret = 'PHW4UZcBhD9fBSyP8Whh2Zz2HRaMRpy3W45vxyU2QBNS7EiAus'
        access_token = '1129945377635913728-FZLi7MCczejWc96FSXAFrY3Bi2KbTB'
        access_token_secret = 'Yw4dP86ESkUpDEPl45RCH9BRlbxpOBPz5m8axnXBfcQrA'

        # Now attempt authentication
        try:
            # Create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # Set access
            self.auth.set_access_token(access_token, access_token_secret)
            # Create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed!")

        # Create Afinn object
        sys.path.insert(0,'../')
        from libraries.afinn.afinn import Afinn
        self._afinn = Afinn()

    def scrape_tweet(self, tweetSingle='', tweetList=[], tweetDict = {}):
        '''
        This is a support function to scrapes a tweet of any unnecessary data
        such as Twitter handles, punctuation, numbers, special characters, and
        short words.
        :param tweetSingle: A single tweet to be cleaned
        :type str:
        :param tweetList: A list of tweets to be cleaned
        :type list:
        :param tweetDict: A dictionary containing {name:tweets} for tweets
        to be cleaned
        :type dictonary:
        :return: Same data type as input but cleaned

        '''
        assert isinstance(tweetDict, dict)
        assert isinstance(tweetList, list)
        assert isinstance(tweetSingle, str)
        
        sr= stopwords.words('english')
        prefixes = ('https')
        lemmatizer = WordNetLemmatizer()
        clean_word = []
        
        if tweetSingle != '':
            temp = tweetSingle.translate(str.maketrans('', '', string.punctuation)).strip()
            cleanedTweet = temp.lower().split()
            for word in cleanedTweet:
                temp = re.sub(r'[^\w\s]', '', word)
                if temp not in sr and len(temp)>2 and not temp.startswith(prefixes):
                    lemma = lemmatizer.lemmatize(temp, pos='v')
                    clean_word.append(lemma)    
            return clean_word
        
        elif len(tweetList) > 0:
            cleanedTweet = []
            for tweet in tweetList:
                temp = tweet.translate(str.maketrans('', '', string.punctuation)).strip()
                cleanedTweet.append(temp.lower().split())
            for line in cleanedTweet:
                for word in line:
                    temp = re.sub(r'[^\w\s]', '', word)
                    if temp not in sr and len(temp)>2 and not temp.startswith(prefixes):
                        lemma = lemmatizer.lemmatize(temp, pos='v')
                        clean_word.append(lemma)    
            return clean_word
        
        elif len(tweetDict) > 0:
            keys = tweetDict.keys()
            clean_dict = dict()
    
            for name in keys:
                for tweet in tweetDict[name]:
                    temp = tweet.translate(str.maketrans('', '', string.punctuation)).strip()
                    if name in clean_dict.keys():
                        clean_dict[name].append(temp.lower().split())
                    else:
                        clean_dict[name] = [temp.lower().split()]
    
            # Next, using NLTK module for text preprocessing, including lemmatizing, removing stopwords such as "a,the,etc",
            # Removing noisy data like http...
    
            for i in clean_dict.keys():
                clean_word = []
                for line in clean_dict[i]:
                    for word in line:
                        temp = re.sub(r'[^\w\s]', '', word)
                        if temp not in sr and len(temp)>2 and not temp.startswith(prefixes):
                            lemma = lemmatizer.lemmatize(temp, pos='v')
                            clean_word.append(lemma)
                clean_dict[i] = clean_word
    
            return clean_dict
        else:
            assert False, 'Error with input type.'
            return None

    def scrape_emoji(self, tweetSingle='', tweetList=[], tweetDict = {}):
        '''
        This is a support function to scrape all the emoji from a user
        :param tweetSingle: A single tweet to be analyzed
        :type str:
        :param tweetList: A list of tweets to be analyzed
        :type list:
        :param tweetDict: A dictionary containing {name:tweets} for tweets to
        be analyzed
        :type dictonary:
        :return: Return a dictionary with key as the user and values as emojilist
        '''
        keys = tweetDict.keys()
        clean_dict = dict()

        for i in keys:
            emojilist = []
            for j in tweetDict[i]:
                temp = j.translate(str.maketrans('', '', string.punctuation)).strip()
                emsplit = emoji.get_emoji_regexp().split(temp)
                for k in emsplit:
                    if k in emoji.UNICODE_EMOJI:
                        emojilist.append(k)
            clean_dict[i] = emojilist

        return clean_dict


    def perform_sentiment_analysis(self, tweetSingle='', tweetList=[], tweetDict = {}):
        '''
        This is a support function to classify sentiment of passed tweet, list
        of tweets, or dictionary of {name:tweets}
        :param tweetSingle: A single tweet to be analyzed
        :type str:
        :param tweetList: A list of tweets to be analyzed
        :type list:
        :param tweetDict: A dictionary containing {name:tweets} for tweets to
        be analyzed
        :type dictonary:
        :return: Returns a single value, list of value or dictionary
        containing {name:value} where the value is a floating point number
        '''

        return None

    def get_data(self, query, count=10, fileName=''):
        '''
        This function is used to fetch tweets, load data from file, or collect
        data. If query='loadData' the date is loaded from the fileName given.
        If query='collectData' the user names for which we want to collect data
        are read in from the csv file specified. Else, we query the user provided
        in query and create a new dictionary.
        :param query: Specified whether to load data, collect or perform a
        single query
        :type str:
        :param count: Number of tweets to collect
        :type int:
        :param fileName: File name to read for loadData or collectData commands
        :type str:
        :return dict: Dictionary with {Name: Tweets}
        '''
        tweetDict = {}
        if query == 'loadData':
            # Open data file and create dict
            assert fileName != '','Error: Please provide file name'
            assert fileName.endswith('.txt'), 'Error: Invalid extension'
            assert os.path.isfile(fileName), 'Error: File does not exist'
            assert isinstance(fileName,str), 'Error: Invalid file name'

            with open(fileName,'rb') as handle:
                tweetDict = pickle.loads(handle.read())

        elif query == 'collectData':
            # Open CSV file and collect data for each name
            assert fileName != '','Error: Please provide file name'
            assert fileName.endswith('.csv'), 'Error: Invalid extension'
            assert os.path.isfile(fileName), 'Error: File does not exist'
            assert isinstance(fileName,str), 'Error: Invalid file name'

            # Read csv file into list.
            with open(fileName, 'r') as f:
                reader = csv.reader(f)
                nameList = list(reader)

            #Collect tweets for every name in the file
            for name in nameList:
                tempDict = self.get_data(name[0], count)
                if '' in tempDict:
                    print('No tweets found for ' + name[0])
                else:
                    print('Found ' + str(len(tempDict[name[0]])) + \
                    ' tweets for ' + name[0])
                    tweetDict.update(tempDict)

        else:
            # Collect 'count' tweets using 'query' as the search term
            assert isinstance(query,str)
            assert isinstance(count, int)
            assert count > 0 , 'Error: Invalid count number'
            try:
                # Call twitter API to fetch tweets
                tweetsJSON = self.api.user_timeline(screen_name=query, \
                count = count, include_rts=False,tweet_mode='extended')

                #Parse each one
                tweetList = []
                screenName = ''
                for tweet in tweetsJSON:
                    tweetList.append(tweet.full_text)
                    screenName = tweet.user.screen_name

                tweetDict[screenName]=tweetList
            except tweepy.TweepError as e:
                print('Error: ' + str(e))

        return tweetDict

    def store_data(self,dictIn, fileName):
        '''
        This is a support function use to write a dictionary to file.
        :param dictIn: Dictionary to write
        :type str:
        :param filename: Name of the file to write, including extension
        :type str:
        :returns None:
        '''
        assert isinstance(dictIn, dict), 'Error: Parameter not a dictionary'
        assert isinstance(fileName, str), 'Error: Invalid filename'
        assert fileName.endswith('.txt'), 'Error: Invalid extension'

        with open(fileName, 'wb') as handle:
            pickle.dump(dictIn,handle)

        return None

def main():
    # Create objects here
    # Insert visualization code here
    pass

if __name__ == "__main__":
    # Calling main function
    main()
