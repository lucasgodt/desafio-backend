import json
from django.http import JsonResponse
from cidades.models import City

# Create your views here.
def index(request):
    if request.method == "GET":
        cidade = City.objects.get(nome="São Paulo")
        cidades = {
            "suggestions": [cidade.serialize(1), cidade.serialize(0.98)]
        }
        return JsonResponse(cidades, json_dumps_params={'ensure_ascii': False}, status=200)
    else:
        return JsonResponse({"error": "GET request required."}, status=400)