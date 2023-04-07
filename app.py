from db.models import Permanencias
from django.db.models import Count,Q


# permanencia = Permanencias.objects.filter(nacimiento='1988-11-04',pais='Rusia')
# print(f'pais: {permanencia[0].pais} comuna: {permanencia[0].comuna} sexo: {permanencia[0].sexo} mes: {permanencia[0].mes} año: {permanencia[0].year} ')

dato = Permanencias.objects.values('comuna').filter(pais='Rusia').annotate(
    cantidad_mujeres=Count('pk',filter=Q(sexo='Femenino')),
    cantidad_hombres=Count('pk',filter=Q(sexo='Masculino'))
    )

for item in dato:
    print(f'comuna: {item["comuna"]} mujeres: {item["cantidad_mujeres"]} hombres: {item["cantidad_hombres"]}')