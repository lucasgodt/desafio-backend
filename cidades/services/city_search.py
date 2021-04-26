from fuzzywuzzy import fuzz
from cidades.models import City

def exact_search(search_entry):
    cidades = City.objects.filter(nome__contains=search_entry)
    if cidades.count() > 0:
        return [cidade.serialize(1) for cidade in cidades]
    return []

def similar_search(search_entry):
    """
    Filter cities by removing one character
    """
    length = len(search_entry)
    score = (length-1)/length
    substrings = [search_entry[0:length-1], search_entry[1:length]]
    cidades = []
    for substring in substrings:
        similar = City.objects.filter(nome__contains=substring).exclude(nome__contains=search_entry)
        if similar.count() > 0:
            for cidade in similar:
                cidades.append(cidade.serialize(score))
    return cidades

def partial_ratio_search(search_entry):
    MINIMUM_TOKEN_SIMILARITY = 75
    all_cities = City.objects.all()
    cidades = []
    for cidade in all_cities:
        similarity = fuzz.partial_ratio(search_entry, cidade.nome)
        if similarity > MINIMUM_TOKEN_SIMILARITY:
            cidades.append(cidade.serialize(similarity/100))
    return cidades

def search(search_entry):
    cidades = []
    
    partial_ratio = partial_ratio_search(search_entry)
    if len(partial_ratio) > 0:
        partial_ratio = sorted(partial_ratio, key=lambda k: k['score'], reverse=True)
        cidades.extend(partial_ratio)
    
    return cidades