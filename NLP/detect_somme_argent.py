# Détection des sommes d'argent
def detect_somme_argent(phrase):
    
    pattern = r"(\s|^)([\d]+(,[\s]*[\d]+)?)[\s]*(keuros|euros|ke|keuro|keu|e)($|\s)"
    
    return re.sub(pattern, ' SOMMEARGENT ', phrase)
