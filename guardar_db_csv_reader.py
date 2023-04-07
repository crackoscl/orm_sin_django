from db.models import Permanencias
from time import time
import csv
from pathlib import Path

inicio = time()

BASE_DIR = Path(__file__).resolve().parent
csv_file = BASE_DIR / 'datos' / 'permanencias_definitivas_otorgadas_2000_al_2011.csv'

with open(csv_file) as file:
    csv_file = csv.reader(file)
    next(csv_file, None)
    
    lista_permanencias = [Permanencias(
        sexo = item[0],
        pais = item[1],
        nacimiento = item[2],
        actividad = item[3],
        profesion = item[4],
        estudios = item[5],
        comuna = item[6],
        provincia = item[7],
        region = item[8],
        tit_dep = item[9],
        autoridad = item[10],
        beneficio_agrupado = item[11],
        year = item[12],
        mes = item[13]
        
    ) for item in csv_file]


Permanencias.objects.bulk_create(lista_permanencias)

print(f'bulk_create {time() - inicio} segundos')