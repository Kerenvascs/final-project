import pandas as pd
import ast, json
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
# Import Punkt
nltk.download('punkt')

tweets_df= pd.read_csv("D:\2.Repositories\Ironhack\Module 3\projects\Final project\final-project\your-project\old_tweets.csv")
tweets_df.head()
