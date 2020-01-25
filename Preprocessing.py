import pandas as pd
import re
from nltk.tokenize import WordPunctTokenizer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

def get_abbreviated_dict():
    abbreviation_dict = {}
    with open("data/singkatan.txt") as file:
        for line in file:
            (abbreviation, phrase ) = line.split("\t")
            abbreviation_dict[abbreviation] = re.sub('\n','',phrase)
    return abbreviation_dict

def regex_filter(text):
    stripped = re.sub(combined_pat, '', text)
    letters_only = re.sub(r'[^\w\s-]','', stripped)
    lower_case = letters_only.lower()
    repeated_char = re.sub(r'([a-z])\1+', r'\1', lower_case)
    return " ".join(repeated_char.split())

def replace_abbreviation(text, abbreviation_dict):
    replaced = ' '.join(str(abbreviation_dict.get(word,word)) for word in text.split())
    return replaced

def remove_stopwords(text):
    words = tokenizer.tokenize(text)
    filtered_words = [word for word in words if not word in stop_words] 
    return (" ".join(filtered_words))

def preprocess_text(text, abbreviation_dict):
    abbreviation_replaced = replace_abbreviation(text, abbreviation_dict)
    regex_filtered = regex_filter(abbreviation_replaced)
    stopwords_removed = remove_stopwords(regex_filtered)
    return stopwords_removed

tokenizer = WordPunctTokenizer()
factory = StopWordRemoverFactory()
stop_words = factory.get_stop_words()

remove_mentions = r'@[A-Za-z0-9_]+' 
remove_links = r'https?://[A-Za-z0-9./]+' 
remove_retweets = r'RT' 
remove_hashtags = r'#[A-Za-z0-9_]+' 
remove_pics = r'pic.twitter.com/[A-Za-z0-9]+'
letters_only = r"[^A-Za-z'\s]"
combined_pat = r'|'.join((remove_mentions,remove_links,remove_retweets,remove_hashtags,remove_pics, letters_only))


data_path = 'data/all_tweets.csv'
tweet_data = pd.read_csv(data_path)

abbreviation_dict = get_abbreviated_dict()
clean_tweets = tweet_data['tweet'].apply(lambda x: preprocess_text(x, abbreviation_dict))
clean_tweets = clean_tweets[clean_tweets.str.count('\s+').gt(3)]
clean_tweets = pd.DataFrame(clean_tweets, columns=['tweet'])

file_name = 'clean_tweets.csv'
clean_tweets.to_csv(file_name, index=False)