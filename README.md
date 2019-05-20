# Analyzing Political Figures' Tweets
This project aims to answer the question "Do political figures have a certain way of speaking given their political affiliation?" 
Our proposed solution is to use sentiment analysis to implement a classification system. There is a theory stating that the sentiment 
of the user can determine the political affiliation and we will determine if that is true. In general, sentiment analysis will categorize
tweets in either positive, neutral, or negative categories. The project will be broken down into the following:
1. Collecting data (extraction)
2. Text pre-processing (cleaning)
3. Sentiment analysis (classification)
4. Data visualization (presentation)

Visualizations can include a breakdown of how certain political figures tend to speak, how they speak on certain issues, and their trends
in language over time and in certain periods of time.

## Getting Started
Perform a git clone, fork, or checkout to get all necessary code. All code performing the four steps above will be available as Python 
functions or classes. Individual unit tests or quick demos can be found under the *test/* folder as Jupyter notebooks (?). 

### Prerequisites

The following are required:
1. Python 3.3 or above (tested with 3.6)
    - [Tweepy](https://github.com/tweepy/tweepy)
    - [afinn](https://github.com/fnielsen/afinn)
2. Jupyter

_Note_: Jupyter **strongly recommends** installing Python and Jupyter using the Anaconda Distribution, which includes Python, the Jupyter
Notebook, and other commonly used packages for scientific computing and data science.

The most recent Anaconda release can be found at: https://www.anaconda.com/distribution/ 

### Installing
#### Jupyter
As stated above, the Python and Jupyter requirements can be satisfied by using the Anaconda Distribution; the link above provides 
instructions on how to do so.

For existing or experienced Python users, Jupyter can be installed using Python's package manager, pip, intead of Anaconda.
```
python3 -m pip install --upgrade pip
python3 -m pip install jupyter
```

To launch the notebook the following command can be used.

```
jupyter notebook
```
#### Afinn
The afinn library is a Wordlist-based approach for sentiment analysis. The library can be found under libraries/afinn and requires no additional installation. Our sentimet_Analysis class imports the library on construction.
Here's a quick test to make sure it is working correctly within our module
```python
from ourCode import sentiment_Analysis
test = sentiment_Analysis()
test._afinn.score('What a great test this is.')
```

#### Tweepy
The Tweepy library is our interface to Twitter, the version used can be found under libraries/tweepy. To use this verion the following can be used:
'''
cd libraries/tweepy
python3 setup.py install
'''
To use the latest version a simple installation can be done with
'''
pip install tweepy
'''
or
'''
git clone https://github.com/tweepy/tweepy.git
cd tweepy
python3 setup.py install
'''

**_TODO_**_After choosing which Python library to use, include instructions here on how to install it.
Also include a few commands to run a quick dem (just to make sure installation is working)._

## Running the tests

**_TODO_**_Explain how to run the automated tests for this system_

### Break down into end to end tests

**_TODO_**_Explain what these tests test and why_

```
Give an example
```

## Authors
* **Amr Elfiky** - *Initial work* - [aselfiky](https://github.com/aselfiky)
* **Tianyi Liu** - *Initial work* - 
* **Yuesong Shi** - *Initial work* - [fantastypea](https://github.com/fantastypea)
* **Edward Zamora** - *Initial work* - [Edward-Zam](https://github.com/Edward-Zam)

See also the list of [contributors](https://github.com/aselfiky/ece143project/contributors) who participated in this project.

## Acknowledgments

* Professor Unpingco
* TA Ambareesh Jayakumari
* TA Erik Seetao
* UCSD ECE Department
