# Money detection
def detect_amount_money(phrase):
    
    pattern = r"(\s|^)([\d]+(,[\s]*[\d]+)?)[\s]*(keuros|euros|ke|keuro|keu|e)($|\s)"
    
    return re.sub(pattern, ' amount_money ', phrase)
