# colocation function for 2 words
def coloc_2(s):
    s = preprocess(s)
    s1 = s.split()
    s1 = list(zip(s1[:-1], s1[1:]))
    s1 = list(map(lambda x: '_'.join(x), s1))
    
    return ' '.join(s1)
    
    
    
# colocation function for 3 words
def coloc_3(s):
    s = preprocess(s)
    s1 = s.split()
    s1 = list(zip(s1[:-2], s1[1:-1], s1[2:]))
    s1 = list(map(lambda x: '_'.join(x), s1))
    
    return ' '.join(s1)    
    

# Calling
data['coloc_2'] = data['text_column'].map(lambda phrase: coloc_2(phrase))
data['coloc_3'] = data['text_column'].map(lambda phrase: coloc_3(phrase))
