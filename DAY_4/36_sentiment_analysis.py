# 36 Sentiment analysis with TF-IDF
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
texts=["I love it","Amazing service","Very happy","I hate it","Poor quality","Very disappointing"]
labels=["positive","positive","positive","negative","negative","negative"]
m=make_pipeline(TfidfVectorizer(),LogisticRegression()).fit(texts,labels)
print(m.predict(["Amazing product","This is poor"]))