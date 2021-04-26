from django.http import JsonResponse
from cidades.services.city_search import search

# Create your views here.
def index(request):
    if request.method == "GET":
        search_entry = request.GET.get("q")
        if search_entry=="":
            return JsonResponse({"error": "Query parameter required."}, status=400)
        suggestions = search(search_entry)
        cidades = {
            "suggestions":  suggestions
        }
        return JsonResponse(cidades, json_dumps_params={'ensure_ascii': False}, status=200)
    else:
        return JsonResponse({"error": "GET request required."}, status=400)