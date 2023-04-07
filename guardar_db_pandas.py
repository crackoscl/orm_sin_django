from db.models import Permanencias
from time import time
import pandas as pd
from pathlib import Path

#insert bulk_create la mas rapida 

inicio = time()

BASE_DIR = Path(__file__).resolve().parent
url = BASE_DIR / 'datos' / 'permanencias_definitivas_otorgadas_2000_al_2011.csv'
dataframe = pd.read_csv(url)

lista_permanencias = [Permanencias(
    sexo = item.SEXO,
    pais = item.PAÍS,
    nacimiento = item.NACIMIENTO,
    actividad = item.ACTIVIDAD,
    profesion = item.PROFESIÓN,
    estudios = item.ESTUDIOS,
    comuna = item.COMUNA,
    provincia = item.PROVINCIA,
    region = item.REGIÓN,
    tit_dep = item.TIT_DEP,
    autoridad = item.AUTORIDAD,
    beneficio_agrupado = item.BENEFICIO_AGRUPADO,
    year = item.AÑO,
    mes = item.MES
        
    ) for item in dataframe.itertuples()]


Permanencias.objects.bulk_create(lista_permanencias)

print(f'bulk_create {time() - inicio} segundos')

