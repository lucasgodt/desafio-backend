from django.db import models

# Create your models here.
class State(models.Model):
    codigo_uf = models.SmallIntegerField()
    uf = models.CharField(max_length=2)
    nome = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)

    class Meta:
        verbose_name_plural = "States"

    def __str__(self) -> str:
        return f"{self.nome} ({self.uf})"

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="city")
    codigo_ibge = models.CharField(max_length=8)
    nome = models.CharField(max_length=40)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)
    capital = models.BooleanField()

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self) -> str:
        return f"{self.nome} - {self.state.uf}"
    
    def serialize(self, score):
        return {
            "name": f"{self.nome} - {self.state.uf}",
            "latitude": self.latitude,
            "longitude": self.longitude,
            "score": score
        }
