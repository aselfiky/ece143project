# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:04:01 2019

@authors: 
    Amr Elfiky 
    Tianyi Liu
    Yuesong Shi
    Edward Zamora 
                
"""

import tweepy 
from tweepy import OAuthHandler 
from afinn import Afinn

class sentimentAnalysis(object):
    '''
    Our main class for twitter interface and sentiment analysis
    '''
    def __init__(self):
        '''
        Construction and initilization
        '''
        #Setup Twitter authentication variables
        # Don't have these values yet
        consumer_key = 'XXXX'
        consumer_secret = 'XXXX'
        access_token = 'XXXX'
        access_token_secret = 'XXXX'
        
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
        
        return None
    
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
        data.
        '''
        if query == 'loadData':
            # Open data file and create dict
            tweetDict = {}
        elif query == 'collectData':
            # Open CSV file and collect data for each name
            tweetDict = {}
        else:
            # Collect 'count' tweets using 'query' as the search term
            try:
                # Call twitter API to fetch tweets
                #Parse each one
                tweetDict = {}
                tweetList = []
                for tweets in tweetsJSON:
                    # Use query as key and store tweets in list
                    # Make sure not to use
                    pass
            except tweepy.TweepError as e:
                print('Error: ' + str(e))
            
        return None
        
    def main():
        # Create objects here
        # Insert visualization code here
        pass
    
    if __name__ == "__main__":
        # Calling main function
        main()
        
    