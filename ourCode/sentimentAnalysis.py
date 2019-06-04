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
import re
import emoji
import pandas as pd
import nltk
#from nltk.tokenize import regexp_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#from afinn import Afinn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy import stats


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
        # download word collections
        assert nltk.download('stopwords'), "Could not download word list 'stopwords'"
        assert nltk.download('wordnet'), "Could not download word list 'wordnet'"

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
        assert isinstance(tweetDict, dict), 'Error: tweetDict must be a dictionary'
        assert isinstance(tweetList, list), 'Error: tweetList must be a list'
        assert isinstance(tweetSingle, str), 'Error: tweetSingle must be a string'

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
                cleaned_tweets = []
                for line in clean_dict[i]:
                    clean_word = []
                    for word in line:
                        temp = re.sub(r'[^\w\s]', '', word)
                        if temp not in sr and len(temp)>2 and not temp.startswith(prefixes):
                            lemma = lemmatizer.lemmatize(temp, pos='v')
                            clean_word.append(lemma)
                    cleaned_tweets.append(clean_word)
                clean_dict[i] = cleaned_tweets

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
        assert isinstance(tweetDict, dict), 'Error: tweetDict must be a dictionary'
        
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


    def perform_sentiment_analysis(self, tweetDict = {}):
        '''
        This is a support function to classify sentiment of passed tweets.

        :param tweetDict: A dictionary containing {name:tweets} for tweets to
        be analyzed
        :type dictonary:
        :return: List of tuples containing (name, score).
        '''
        assert isinstance(tweetDict, dict), 'Error: tweetDict must be a dictionary'

        results = {}
        # for each candidate analyze all their words on tweet by tweet basis
        for name, tweets in tweetDict.items():
            total_score = 0
            count = 0
            for tweet in tweets:
                total_score = total_score + self._afinn.score(' '.join(word for word in tweet))
                count = count + 1
            results[name] = total_score/count

        return results

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

    def get_sentimental_words(self, dictIn):
        '''
        This is a support function that eliminates words that cannot determine
        sentiment, such as nouns.
        :param dictIn: Dictionary to tag
        :type dict:
        :returns set: Words that can determine sentiment (e.g., adjectives, adverbs)
        '''
        assert isinstance(dictIn, dict), 'Error: Parameter not a dictionary'

        # parts of speech that can determine sentiment
        describing_pos = ['RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS']
        tagged = []

        # tag pos for every word from the tweets
        for name, words in dictIn.items():
            tweet = nltk.pos_tag(words)
            tweet = [x[0] for x in tweet if x[1] in describing_pos]
            tagged.append(tweet)

        # only take unique words that can determine sentiment
        bag_of_words = []
        for tagged_tweets in tagged:
            bag_of_words = set(list(bag_of_words) + tagged_tweets)

        return bag_of_words

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

    def create_visualizations(self):
        '''
        This main function creates the visualizations used for the presentation.
        '''
        # Instead of querying Twitter everytime we run this, just load data from a 
        # previous data collection.
        # Create object of class
        sentimentObject = sentiment_Analysis()
        
        # Load dictionary with {name, party} and dictionary with {name, dirty Tweets}
        spDict = sentimentObject.get_data('loadData', fileName = "../data/senateParty.txt")
        stDict = sentimentObject.get_data('loadData', fileName = "../data/senateTweets.txt")
            
        # Clean dictionary
        stcDict = sentimentObject.scrape_tweet(tweetDict = stDict)
        
        # Analyze sentiment 
        ssDict = sentimentObject.perform_sentiment_analysis(stcDict)
        
        stcDDict = {}  # This is the dict containing all the Democrat senators and their clean tweets
        stcRDict = {}  # Republic senators and their clean tweets
        for key in stcDict:
            if spDict[key] == 'D':
                stcDDict[key] = stcDict[key]
            elif spDict[key] == 'R':
                stcRDict[key] = stcDict[key]
        
        sDDict = {}  # This is the dict containing all the Democrat senators and their sentiment scores
        sRDict = {}  # Republic senators adn their scores
        for key in ssDict:
            if spDict[key] == 'D':
                sDDict[key] = ssDict[key]
            elif spDict[key] == 'R':
                sRDict[key] = ssDict[key]
            
        # Create plots
        #creat a list for only sentiment scores
        sslist = [v for v in ssDict.values()]
        sDlist = [v for v in sDDict.values()]
        sRlist = [v for v in sRDict.values()]
        
        plt.rcParams.update({'font.size': 14})
        plt.figure(1)  # bar graph of all sentiment score and two parties separately
        plt.hist(sDlist,color='b',label='Democratic')
        plt.hist(sRlist,color='r',label='Republican')
        plt.xticks(np.arange(-2,7,0.5))
        plt.title('Sentiment score by party')
        plt.xlabel('score')
        plt.ylabel('frequency')
        plt.legend(loc='upper right')
        #plt.show()
        
        plt.figure(2)
        
        plt.hist(sDlist,color='b',label='Democratic')
        plt.title('Sentiment score of the Democratic Party')
        plt.xticks(np.arange(-2,7,0.5))
        plt.xlabel('score')
        plt.ylabel('frequency')
        #plt.show()
        
        plt.figure(3)
        plt.hist(sRlist,color='r',label='Republican')
        plt.xticks(np.arange(-2,7,0.5))
        plt.xlabel('score')
        plt.ylabel('frequency')
        plt.title('Sentiment score of Republican Party')
        #plt.show()
    
        # (2)mean deviation,std,of two parties' score
        scoreD = [v for v in sDDict.values()]  # The score of Democratic party
        scoreR = [v for v in sDDict.values()]  # The score of Republic party
        print(scoreD)
        print(scoreR)
        
        D = np.array(scoreD)
        R = np.array(scoreR)
        col_labels = ['Democratic Party', 'Republican Party']
        row_labels = ['max', 'min', 'mean', 'median', 'mode', 'variance', 'std deviation']
        col_colors = ['blue', 'red']
        
        # get max, min, mean, median, mode, std for democrat and republican results
        max = [np.amax(D), np.amax(R)]
        min = [np.amin(D), np.amin(R)]
        mean = [np.mean(D), np.mean(R)]
        median = [np.median(D), np.median(R)]
        mode = [stats.mode(D)[0][0], stats.mode(R)[0][0]]
        variance = [np.var(D), np.var(R)]
        std = [np.std(D), np.std(R)]
        
        table_vals = np.around([max, min, mean, median, mode, variance, std], decimals=3)
        print(table_vals)
        
        plt.figure(4)
        plt.table(cellText=table_vals, cellLoc='center',rowLabels=row_labels, colLabels=col_labels,
                  colColours=col_colors,colWidths=[0.4 for x in range(len(table_vals))], loc='best')
        plt.title('Statistics')
        plt.axis('off')
        
        # (3)box graph for two party
        labels = ['Democratic','Republican']
        color = dict(boxes = "DarkGreen", whiskers = "DarkOrange", medians = "DarkBlue", caps = "Gray")
        plt.figure(5)
        plt.boxplot([D,R],labels=labels,sym='o')
        plt.title('Box plot')
        
        # create two txt files that only contains the clean tweets of two parties.
        #afinn = Afinn()
        D = open('stcD.txt', 'w+',encoding='utf-8')
        for key in stcDDict:
            for item in stcDDict[key]:
                for element in item:
                    if self._afinn.score(element) != 0:
                        D.write(element)
                        D.write('\n')
        
        
        D.close()
        
        R = open('stcR.txt', 'w+',encoding='utf-8')
        for key in stcRDict:
            for item in stcRDict[key]:
                for element in item:
                    if self._afinn.score(element) != 0:
                        R.write(element)
                        R.write('\n')
        
        D.close()
        
        
        #word cloud for two parties
        plt.figure(6)
        textD = open(r'./stcD.txt','r').read()
        wcD = WordCloud(background_color='white', scale=1.5).generate(textD)
        plt.imshow(wcD)
        #plt.title('Word cloud of Democratic Party')
        plt.axis('off')
        
        plt.figure(7)
        textR = open(r'./stcR.txt','r').read()
        wcR = WordCloud(background_color='white', scale=1.5).generate(textR)
        plt.imshow(wcR)
        #plt.title('Word cloud of Republican Party')
        plt.axis('off')
        plt.show()
        