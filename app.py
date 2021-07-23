import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recomend',methods=['POST'])
def recomend():
    '''
    For rendering results on HTML GUI
    '''
    m = [str(x) for x in request.form.values()]
    
    
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
    
    
    m=m[0]
    m=m.lower()
    
    truval = m in df['Title'].unique()        
    if truval==True:
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
        output=m
        return render_template('index.html', recomended_movies='Recomended movies are $ {}'.format(output))
    if truval==False:
        return render_template('index.html', recomended_movies='Invalid Movie Name')
   


if __name__ == "__main__":
    app.run(debug=True)
