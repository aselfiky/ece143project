# noinspection PyUnresolvedReferences

import pickle
import pandas as pd
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy import stats
from sentimentAnalysis import sentiment_Analysis
from afinn import Afinn

"""
@authors:
    Amr Elfiky
    Tianyi Lu
    Yuesong Shi
    Edward Zamora

This is the visualization of the data we have gathered and analyzed.
"""

with open(r'../data/senateParty.txt', 'rb') as sp:
    spDict = pickle.loads(sp.read())

with open(r'../data/senateTweets.txt', 'rb') as st:
    stDict = pickle.loads(st.read())

with open(r'../data/senateTweetsClean.txt', 'rb') as stc:
    stcDict = pickle.loads(stc.read())

stcDDict = {}  # This is the dict containing all the Democrat senators and their clean tweets
stcRDict = {}  # Republic senators and their clean tweets
for key in stcDict:
    if spDict[key] == 'D':
        stcDDict[key] = stcDict[key]
    elif spDict[key] == 'R':
        stcRDict[key] = stcDict[key]

with open(r'../data/senateSentiments.txt', 'rb') as ss:
    ssDict = pickle.loads(ss.read())

sDDict = {}  # This is the dict containing all the Democrat senators and their sentiment scores
sRDict = {}  # Republic senators adn their scores
for key in ssDict:
    if spDict[key] == 'D':
        sDDict[key] = ssDict[key]
    elif spDict[key] == 'R':
        sRDict[key] = ssDict[key]


plt.rcParams.update({'font.size': 14})
plt.figure(1)  # bar graph of all sentiment score and two parties separately
i = 0
for key in ssDict:
    if spDict[key] == 'D':
        plt.bar(i, ssDict[key], color='b')
    elif spDict[key] == 'R':
        plt.bar(i, ssDict[key], color='r')

    i = i + 1

plt.title('Sentiment score by party')
plt.xlabel('senators')
plt.ylabel('score')
#plt.show()

plt.figure(2)
i = 0
for key in sDDict:
    plt.bar(i,sDDict[key],color='b')
    i = i+1

plt.title('Sentiment score of the Democratic Party')
plt.ylabel('score')
plt.xlabel('senators')

plt.figure(3)
i = 0
for key in sRDict:
    plt.bar(i,sRDict[key],color='r')
    i = i+1

plt.title('Sentiment score of Republican Party')
plt.ylabel('score')
plt.xlabel('senators')

# (2)mean deviation,std,of two parties' score
scoreD = [v for v in sDDict.values()]  # The score of Democratic party
scoreR = [v for v in sDDict.values()]  # The score of Republic party
print(scoreD)
print(scoreR)

D = array(scoreD)
R = array(scoreR)
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
afinn = Afinn()
D = open('stcD.txt', 'w+',encoding='utf-8')
for key in stcDDict:
    for item in stcDDict[key]:
        for element in item:
            if afinn.score(element) != 0:
                D.write(element)
                D.write('\n')


D.close()

R = open('stcR.txt', 'w+',encoding='utf-8')
for key in stcRDict:
    for item in stcRDict[key]:
        for element in item:
            if afinn.score(element) != 0:
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
