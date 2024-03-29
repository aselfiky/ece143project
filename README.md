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
functions or classes. Individual unit tests or quick demos can be found under the *jupyterTests/* folder as Jupyter notebooks. 

### Prerequisites

The following are required:
1. Python 3.3 or above (tested with 3.6)
    - [Tweepy](https://github.com/tweepy/tweepy)
    - [afinn](https://github.com/fnielsen/afinn)
    - [NLTK](https://www.nltk.org/)
    - [emoji](https://github.com/carpedm20/emoji)
    - [wordcloud](https://pypi.org/project/wordcloud/)
    - [HoloViews](https://github.com/pyviz/holoviews/blob/master/LICENSE.txt)
    - [hvPlot](https://github.com/pyviz/hvplot)
    
    
    
    
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
```
cd libraries/tweepy
python3 setup.py install
```
To use the latest version a simple installation can be done with
```
pip install tweepy
```
or
```
git clone https://github.com/tweepy/tweepy.git
cd tweepy
python3 setup.py install
```
#### NLTK
NLTK is a platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning. We mainly use this module for text preprocessing and tagging the tweets. 

The interactive installer can be initiated using:
```
import nltk
nltk.download()
```
Or you can download specific modules used by calling:
```
import nltk
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')
```

#### EMOJI
This module is used to extract all emoji used by a user. To use emoji module, the installation can be done with:
```
pip install emoji --upgrade
```

#### Wordcloud
This module is use to create the wordclouds used in our presentation. The use the wordcloud module, the installation can be done with:
```
pip install wordcloud
```

#### HoloViews and hvPlot
HoloViews was used for the emoji plot visualizations but it is not required for the rest of the code. It can be installed through the anaconda installer or pip. hvPlot is a plotting API for data containers built with HoloViews, it works alongside HoloViews and is only required for visualizations in our code.
Using the Conda command:
```
conda install -c pyviz holoviews bokeh
conda install -c pyviz hvplot
```
Using pip:
```
pip install "holoviews[recommended]"
pip install hvplot
```

### Running the tests
Unit tests are included in the _jupyterTests/_ directory. These tests assume 3rd party libraries are installed within the _libraries/_ directory but should work even if they are not (as long as their respective setup.py files were used to setup correct paths). You can use these tests as reference or run them directly from a Jupyter notebook.
### Unit Tests - Interface to Twitter, data collection/storage and data cleaning
We have included a set of unit tests of some of the individual methods of our class; these tests are for the collection, storage, loading, and cleaning methods of our class and can be found in the _juptyetTests/unit_tests.ipynb_ file. The *get_data()* method provides a simple interface to Twitter and supports the following:
+ Perform a single query to collect a certain amount of Tweets from a user (count and user are specified)
+ Load saved Tweets from a file (stored using the *store_data()* method)
+ Read a _.csv_ file with user names and collect Tweets from all corresponding users (count can be specified)

As stated above, the *store_data()* method can be used to save these Tweets to a file (as a dictionary) and a unit test for this is also provided in the same Jupyter notebook.

Once this data is collected (or loaded) we can test the data scrapping and emoji extraction methods from our class. 

### Visualizations
Visualizations for the presentation found in _presentation/Analysing Political Figures' Tweets.pptx_. The main fuction of our class creates these visualizations and can be run with the following commands.

```
python3 
from ourCode import sentiment_Analysis
testObject = sentiment_Analysis()
testObject.create_visualizations()
```

As a convenience and requirement, the code to generate the visualizations used in the presentations can also be found in the Jupyter notebook in _jupyterTests/visualizations.ipynb_

## Authors
* **Amr Elfiky** - *Initial work* - [aselfiky](https://github.com/aselfiky)
* **Tianyi Lu** - *Initial work* - [Tianyi Lu](https://github.com/t1lu)
* **Yuesong Shi** - *Initial work* - [fantastypea](https://github.com/fantastypea)
* **Edward Zamora** - *Initial work* - [Edward-Zam](https://github.com/Edward-Zam)

See also the list of [contributors](https://github.com/aselfiky/ece143project/contributors) who participated in this project.

## Acknowledgments

* Professor Unpingco
* TA Ambareesh Jayakumari
* TA Erik Seetao
* UCSD ECE Department
