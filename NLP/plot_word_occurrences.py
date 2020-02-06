import matplotlib.pyplot as plt

import itertools

# d1 = {'a':1,'n':2}
# d2 = {'b':1,'n':2}
# print ({ k: d1.get(k, 0) + d2.get(k, 0) for k in set(d1) | set(d2) })
# output = {'a': 1, 'n': 4, 'b': 1}


def vocab(df, column1, column2, nb_mots, stopwords):
    
    vocab_1 = df[column1].str.split(expand=True).stack().value_counts().head(50).to_dict()
    vocab_2 = df[column2].str.split(expand=True).stack().value_counts().head(50).to_dict()
    
    vocab = { k: vocab_1.get(k, 0) + vocab_2.get(k, 0) for k in set(vocab_1) | set(vocab_2) }
    
    vocab = dict(sorted(vocab.items(),key=lambda x: x[1], reverse=True))
    
    vocab_sw = {key:value for (key,value) in vocab.items() if key not in stopwords}
   
    return dict(itertools.islice(vocab_sw.items(), nb_mots))
   
   
   
def plot_words(vocab):

  '''
    vocab is a dictionnary (output of vocab())
  '''
    plt.rcParams['figure.figsize'] = (20, 10)
    plt.show()

    plt.xlim(0,len(vocab))
    plt.xticks(rotation=90,fontsize=14)
    plt.bar(vocab.keys(), vocab.values(), width=0.3, color='g')
