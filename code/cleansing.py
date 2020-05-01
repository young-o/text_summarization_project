import numpy as np
import pandas as pd
path = "/Users/seungyoungoh/workspace/text_summarization_project/"
data = pd.read_csv(path+"/data/news_data.csv", error_bad_lines = False, encoding = 'cp949')

data.columns
# Index(['Unnamed: 0', 'key_point', 'body', 'category', 'url'], dtype='object')

news = data[['key_point', 'body']]
len(news)
# 7377

news.dropna(axis=0, inplace=True)
len(news)
# 5235

print(data['key_point'].nunique())
# 3787
news.drop_duplicates(subset=['key_point'], inplace=True)
len(news)
# 3787

print(data.isnull().sum())
# key_point    0
# body         0

s = news.sample(1)
news.to_csv(path+"/data/sample.csv", mode='w')
