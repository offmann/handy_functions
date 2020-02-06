from wordcloud import WordCloud
import matplotlib.pyplot as plt



def nuage_mots(df, column1, column2):
    
    df[column1].dropna(inplace=True)
    df[column1] = df[column1].astype(str)
    
    
    text = ' '.join(str(comment) for comment in df[colonne1])
    
    if column2:
        text2 = ' '.join(str(comment) for comment in df[column2])
        df[column2].dropna(inplace=True)
        df[column2] = df[column2].astype(str)
        text = text + text2
    
    wordcloud = WordCloud(stopwords=stopwords, width=800, height=400, background_color="white",max_words=70).generate(text)
    
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.rcParams['figure.figsize'] = (14, 8)
    plt.axis("off")
    plt.show()    
