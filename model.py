import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import sklearn

df=pd.read_csv('bollywood.csv')

df=df.loc[df['Year']>1990]


df=df.reset_index().drop('index',1)

df.isnull().sum(axis=0)

df['Genre']=df['Genre'].replace(np.nan,'unknown')

df['Genre']=df['Genre'].str.replace(',',' ')
df['Cast']=df['Cast'].str.replace(',',' ')
df['Director']=df['Director'].str.replace(' ','')
df['Title']=df['Title'].str.lower()
df['Year']=df['Year'].astype(str)
df['Comb']=df['Year']+' '+df['Director']+' '+df['Genre']+' '+df['Cast']
df['Comb'].head()

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv=CountVectorizer()
count_matrix=cv.fit_transform(df['Comb'])
sim=cosine_similarity(count_matrix)
sim

m='Jab Tak Hai Jaan'
m=m.lower()
m in df['Title'].unique()

i=df.loc[df['Title']==m].index[0]
print(i)
sim[i]
lst=list(enumerate(sim[i]))

lst[:10]
lst=sorted(lst,key=lambda x:x[1],reverse=True)
lst=lst[1:11]

m=[]
for i in range(len(lst)):
    a=lst[i][0]
    m.append(df['Title'][a])
for i in m:
    print(i)
    


