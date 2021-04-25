import json
from django.test import TransactionTestCase
from cidades.models import State, City

# Create your tests here.
class SuggestionsTestCase(TransactionTestCase):
    def setUp(self):
        sp = State(
            codigo_uf=35,
            uf="SP",
            nome="São Paulo",
            latitude=-22.19,
            longitude=-48.79
        )
        sp.save()
        City.objects.create(
            state=sp,
            codigo_ibge="3550308",
            nome="São Paulo",
            latitude=-23.5329,
            longitude=-46.6395,
            capital=True
        )
        City.objects.create(
            state=sp,
            codigo_ibge="3550308",
            nome="Campinas do Sul",
            latitude=-23,
            longitude=-46,
            capital=False
        )
        City.objects.create(
            state=sp,
            codigo_ibge="3550308",
            nome="Campinas do Piauí",
            latitude=-23,
            longitude=-46,
            capital=False
        )
        City.objects.create(
            state=sp,
            codigo_ibge="3550308",
            nome="Campinas",
            latitude=-23,
            longitude=-46,
            capital=False
        )
        City.objects.create(
            state=sp,
            codigo_ibge="3550308",
            nome="Campina",
            latitude=-23,
            longitude=-46,
            capital=False
        )

    def test_response_with_existing_city(self):
        response = self.client.get('/suggestions/', {
            'q':'Campinas'
        })
        self.assertEqual(response.status_code, 200)
        responseJSON = json.loads(response.content)
        self.assertEqual(responseJSON["suggestions"][0]["score"], 1)
    
    def test_response_non_with_existing_city(self):
        response = self.client.get('/suggestions/', {
            'q':'UmaCidadeAleatoriaNoMeioDoNada'
        })
        self.assertEqual(response.status_code, 200)
        responseJSON = json.loads(response.content)
        self.assertEqual(len(responseJSON["suggestions"]), 0)