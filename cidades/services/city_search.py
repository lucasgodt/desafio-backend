from cidades.models import City

def exact_search(search_entry):
    cidades = City.objects.filter(nome__contains=search_entry)
    if cidades.count() > 0:
        return [cidade.serialize(1) for cidade in cidades]
    return None

def search(search_entry):
    cidades = []

    exact = exact_search(search_entry)
    if exact is not None:
        cidades.append(exact)
    
    return cidades