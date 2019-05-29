# noinspection PyUnresolvedReferences

import pickle
import pandas as pd
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy import stats
from sentimentAnalysis import sentiment_Analysis
"""
@authors:
    Amr Elfiky
    Tianyi Lu
    Yuesong Shi
    Edward Zamora

"""
"""
This is the visualization of the data we get
"""
with open(r'C:\Users\zzxxlty\Desktop\ece143project-master\data\senateParty.txt', 'rb') as sp:
    spDict = pickle.loads(sp.read())
    # print(spDict)

with open(r'C:\Users\zzxxlty\Desktop\ece143project-master\data\senateTweets.txt', 'rb') as st:
    stDict = pickle.loads(st.read())
    # print(stDict)

with open(r'C:\Users\zzxxlty\Desktop\ece143project-master\data\senateTweetsClean.txt', 'rb') as stc:
    stcDict = pickle.loads(stc.read())
    # print(stcDict)

stcDDict = {}  # This is the dict containing all the Democrat senators and their clean tweets
stcRDict = {}  # Republic senators and their clean tweets
for key in stcDict:
    if spDict[key] == 'D':
        stcDDict[key] = stcDict[key]
    elif spDict[key] == 'R':
        stcRDict[key] = stcDict[key]

with open(r'C:\Users\zzxxlty\Desktop\ece143project-master\data\senateSentiments.txt', 'rb') as ss:
    ssDict = pickle.loads(ss.read())
    # print(ssDict)

sDDict = {}  # This is the dict containing all the Democrat senators and their sentiment scores
sRDict = {}  # Republic senators adn their scores
for key in ssDict:
    if spDict[key] == 'D':
        sDDict[key] = ssDict[key]
    elif spDict[key] == 'R':
        sRDict[key] = ssDict[key]

# print(sDDict)
# print(sRDict)
#creat a list for only sentiment scores
sslist = [v for v in ssDict.values()]
sDlist = [v for v in sDDict.values()]
sRlist = [v for v in sRDict.values()]

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
scoreD = []  # The score of Democratic party
scoreR = []  # The score of Republic party
scoreD = [v for v in sDDict.values()]
scoreR = [v for v in sRDict.values()]
print(scoreD)
print(scoreR)

D = array(scoreD)
R = array(scoreR)
col_labels = ['Democratic Party', 'Republican Party']
row_labels = ['max', 'min', 'mean', 'median', 'mode', 'variance', 'std deviation']
col_colors = ['blue', 'red']

max = []
max.append(np.amax(D))
max.append(np.amax(R))
print(max)

min = []
min.append(np.amin(D))
min.append(np.amin(R))
print(min)

mean = []
mean.append(np.mean(D))
mean.append(np.mean(R))
print(mean)

median = []
median.append(np.median(D))
median.append(np.median(R))
print(median)

mode = []
mode.append(stats.mode(D)[0][0])
mode.append(stats.mode(R)[0][0])
print(mode)

variance = []
variance.append(np.var(D))
variance.append(np.var(R))
print(variance)

std = []
std.append(np.std(D))
std.append(np.std(R))
print(std)

table_vals = [max, min, mean, median, mode, variance, std]
print(table_vals)

plt.figure(4)
plt.table(cellText=table_vals, cellLoc='center',rowLabels=row_labels, colLabels=col_labels, colColours=col_colors,loc='best')
plt.title('Statistics')
plt.axis('off')
#plt.show()


# (3)box graph for two party
labels = ['Democratic','Republican']
color = dict(boxes = "DarkGreen", whiskers = "DarkOrange", medians = "DarkBlue", caps = "Gray")
plt.figure(5)
plt.boxplot([D,R],labels=labels,sym='o')
plt.title('Box plot')
#plt.show()

# stcDDict
# stcRDict
# create two txt files that only contains the clean tweets of two parties.
D = open('stcD.txt', 'w+',encoding='utf-8')
for key in stcDDict:
    for item in stcDDict[key]:
        for element in item:
            D.write(element)
            D.write('\n')


D.close()

R = open('stcR.txt', 'w+',encoding='utf-8')
for key in stcRDict:
    for item in stcRDict[key]:
        for element in item:
            R.write(element)
            R.write('\n')


D.close()


# word cloud for two parties
plt.figure(6)
textD = open(r'C:\Users\zzxxlty\Desktop\ece143project-master\ourCode\stcD.txt','r').read()
wcD = WordCloud(background_color='white', scale=1.5).generate(textD)
plt.imshow(wcD)
plt.title('Word cloud of Democratic Party')
plt.axis('off')
#plt.show()

plt.figure(7)
textR = open(r'C:\Users\zzxxlty\Desktop\ece143project-master\ourCode\stcR.txt','r').read()
wcR = WordCloud(background_color='white', scale=1.5).generate(textR)
plt.imshow(wcR)
plt.title('Word cloud of Republican Party')
plt.axis('off')
plt.show()
