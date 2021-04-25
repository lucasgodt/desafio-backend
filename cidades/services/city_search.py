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

def search(search_entry):
    cidades = []

    exact = exact_search(search_entry)
    if len(exact) > 0:
        cidades.extend(exact)
    
    similar = similar_search(search_entry)
    if len(similar) > 0:
        cidades.extend(similar)
    
    return cidades