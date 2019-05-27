# ECE 143: Analyzing Political Figure's Tweets [TODO List]

|Task ID  | Task    | Est. Time to Completion |  Assigned To | Notes |
|---------| --------|-------------------------|--------------|-------|
|1        | ~~Assess twitter <--> Python interfaces and choose what to use~~ | 2-3 days | Edward | Can we use libraries or do we interface with Twitter's API directly? Need to ask professor|
|2        | ~~Assess data to be collected~~ | 2-3 days | Amr, Edward | How many political figure's data do we want to collect? Who do we want to collect? Do we need training data? |
|3        | ~~Evaluate different storage methods for data~~| 1-2 days | All | Do we want to store data as text, JSON, or csv file? What data type do we store it as in memory (list, dict, etc)?|
|4        | Collect data that was chosen in 2) using method from 1) and store in method from 3)| 2-3 days | Edward | |
|5        | ~~Text preprocessing (scrapping)~~ | 3-4 days | Yuesong | Develop code to 'scrape' data and only gather what we need (i.e. do we need timestamps, hashtags, or just text?)|
|6        | ~~Assess sentinent analysis~~ | 1-2 days |Amr, Edward| Similar to 1). Can we use a library for this or should we write our own?|
|7        | ~~Perform sentinent analysis~~ | 3-4 days |Amr | If we need to write our own, add a couple more days to Est. completion time|\
|8        | Create Visualizations / PPT | 4-5 days | Tianyi | As this is what we are presenting, we probably want to spend more time on this.|


_Additional Notes_ 
* As stated above, we want to ask the professor/TAs if we are allowed to use 3rd party libraries or expected to write our own code for the
twitter/python interface and for the sentinent analysis.
* If we can use 3rd party libraries then [python-twitter](https://github.com/bear/python-twitter "python-twitter")
and [Twython](https://github.com/ryanmcgrath/twython "Twython") are good candidates. [Afinn](https://github.com/fnielsen/afinn "Afinn") 
seems like a good option for the sentinent analysis.
* If we want to answer the question "Can we guess the political leanings of a person based on their tweets?" then we will need test and training 
data. If we are just looking for general trends then we only need test data.
