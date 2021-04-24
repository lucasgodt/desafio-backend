from django.core.management.base import BaseCommand, CommandError
from cidades.models import State, City
import os
import csv

def populate_state():
    path = "data/states.csv"
    with open(path, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        for row in reader:
            State.objects.create(
                codigo_uf=row[0],
                uf=row[1],
                nome=row[2],
                latitude=row[3],
                longitude=row[4]
            )

def populate_city():
    path = "data/cities.csv"
    with open(path, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        for row in reader:
            state = State.objects.filter(codigo_uf=row[5]).first()
            City.objects.create(
                codigo_ibge=row[0],
                nome=row[1],
                latitude=row[2],
                longitude=row[3],
                capital=True if row[4]==1 else False,
                state=state
            )

class Command(BaseCommand):
    help = 'Import cities and states csv data to populate the database'

    def handle(self, *args, **options):
        populate_state()
        populate_city()
        self.stdout.write(self.style.SUCCESS(f"Create file for 1"))