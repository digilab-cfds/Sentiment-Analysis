import pandas as pd 

def open_file(file_path):
    with open(file_path) as file:
    for line in file:
        [word_id, sentiment] = line.split(':')
        sentiwords['id'].append(word_id)
        sentiwords['sentiment'].append(sentiment[:-1])
        
def drop_duplicates(data_frame,subset):
    if subset == None:
        return data_frame.drop_duplicates()
    else:
        return data_frame.drop_duplicates(subset=subset)
    
    
sentiwords  = {'id':[],
               'sentiment': []}
boosters    = {'id':[],
               'sentiment': []}

id_sentiment_lexicon = pd.DataFrame()


neg_pos_sentiment = pd.read_csv('neg-pos.csv')
opinion_words = pd.read_csv('opinion-words-translated-id.csv', names=['id','sentiment'])

sentiment_words = open_file("sentiwords_id.txt")
sentiment_words_df = pd.DataFrame(sentiment_words)

booster_words = open_file("boosterwords_id.txt")
booster_words_df = pd.DataFrame(booster_words)

opinion_words['id'] = [word.lower() for word in opinion_words['id']]
opinion_words = drop_duplicates(opinion_words, None)

id_sentiment_lexicon = opinion_words.append(booster_words_df, ignore_index=True)
id_sentiment_lexicon = id_sentiment_lexicon.append(neg_pos_sentiment, ignore_index=True)
id_sentiment_lexicon = drop_duplicates(id_sentiment_lexicon,'id')

for values in enumerate(sentiment_words_df.values):
    word = values[1][0]
    sentiment = values[1][1]
    if word in id_sentiment_lexicon['id'].values:
        id_sentiment_lexicon['sentiment'][id_sentiment_lexicon['id']==word] = sentiment
    else :
        id_sentiment_lexicon = id_sentiment_lexicon.append(sentiment_words_df[sentiment_words_df['id']==word], ignore_index=True)
        
id_sentiment_lexicon = id_sentiment_lexicon.sort_values(by=['id'])
id_sentiment_lexicon = id_sentiment_lexicon.reset_index(drop=True)

file_name = 'id_sentiment_lexicon.csv'
id_sentiment_lexicon.to_csv(file_name, index=False)
