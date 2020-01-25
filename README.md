# Sentiment-Analysis

## 1. Text Preprocessing
Text preprocessing for tweets data is done as follows :
1. Remove mentions
2. Remove links
3. Remove RT
4. Remove hashtags
5. Remove image link
6. Remove non alphabet characters (numbers and punctuations)
7. Lower casing
8. Remove repeated characters
9. Replace abbreviation words
10. Remove stopwords

### 1.1 Prerequisites
- Pandas
- NLTK
- Sastrawi
  
  `pip install sastrawi`


## 2. Lexicon Dictionary
The lexicon dictionary that used in this implementation is the combination from a few sources :
1. Opinion Lexicon :
A list of English positive and negative opinion words or sentiment words (around 6800 words).(Hu and Liu, KDD-2004).
In this implementation, the Opinion Lexicon are translated to Indonesian.
https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html

2. ID-OpinionWords :
List of Opinion Words (positive/negative) in Bahasa Indonesia. Originated by Liu's Opinion Words list with modification/translation to Indonesia.
https://github.com/masdevid/ID-OpinionWords 

3. Indonesian sentiment words :
The list of Indonesian sentiment words from a research paper [1].
https://github.com/masdevid/sentistrength_id



References
1. Wahid, D. H., & Azhari, S. N. (2016). Peringkasan Sentimen Esktraktif di Twitter Menggunakan Hybrid TF-IDF dan Cosine Similarity. IJCCS (Indonesian Journal of Computing and Cybernetics Systems), 10(2), 207-218.

