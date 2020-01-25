import pandas as pd
from tqdm import tqdm

def get_sentiment(tweet):
    score = 0
    word_sentiment= []
    for w in tweet:
        try :
            sentiment = (int(lexicon_dict['sentiment'][lexicon_dict['id']==w]))
            score += sentiment
            word_sentiment.append((w,sentiment))
        except:
            score += 0
    if score>0:
        sentiment = 1
    elif score<0:
        sentiment = -1
    else:
        sentiment = 0
    return sentiment, word_sentiment

lexicon_dict_path = 'data/id_sentiment_new.csv'
data_path = 'clean_tweets_labeled.csv'
save_file_name = 'prediction_lexicon_based.xlsx'

prediction = []
word_sentiment = []

lexicon_dict = pd.read_csv(lexicon_dict_path)
data = pd.read_csv(data_path)

for tweet in tqdm(data['Posts']):
    sentiment, word_sent = get_sentiment(tweet)
    prediction.append(sentiment)
    word_sentiment.append(word_sent)
    
data['predict_sentiment'] = prediction
data['word_sentiment'] = word_sentiment

accuracy = len(data[data['sentiment']==data['predict_sentiment']])/len(data)

data.to_excel(save_file_name, index=False)