# Exploratory text Analysis

def eda(df, column, nb_words_display, max_words=100, min_words=20, max_min_freq=True):
    
    '''
    Goal : Apply this function on a column containing text in order to explore the data, the words, nb of occurences
    '''
    
    # number of words in each observation
    df['nb_words'] = df[column].map(lambda sentence: len(sentence.split()))
    print(df['nb_words'].describe())

    # nb of words in the whole corpus
    series = df[column].str.split(expand=True).stack().value_counts()

    # display the most frequent words (default)
    if max_min_freq:
        print(series[:nb_words_display])
        pyplot.scatter(range(nb_words_display), series[:nb_words_display], c = 'red')

    # Display the least frequent words
    else:
        subseries = series.where(series<max_words).where(series>min_words).dropna()
        print(subseries[:nb_words_display])
        pyplot.figure(figsize=(10, 6))
        pyplot.scatter(range(len(subseries)), subseries, c = 'red')
