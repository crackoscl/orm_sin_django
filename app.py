from db.models import Permanencias
from django.db.models import Count,Q


# permanencia = Permanencias.objects.filter(nacimiento='1988-11-04',pais='Rusia')
# print(f'pais: {permanencia[0].pais} comuna: {permanencia[0].comuna} sexo: {permanencia[0].sexo} mes: {permanencia[0].mes} año: {permanencia[0].year} ')

cantidad_de_personas_por_comuna = Permanencias.objects.values('comuna').filter(pais='Rusia').annotate(
    cantidad_mujeres=Count('pk',filter=Q(sexo='Femenino')),
    cantidad_hombres=Count('pk',filter=Q(sexo='Masculino'))
    )

cantidad_de_personas_por_pais = Permanencias.objects.values('pais').annotate(
    cantidad_mujeres=Count('pk',filter=Q(sexo='Femenino')),
    cantidad_hombres=Count('pk',filter=Q(sexo='Masculino'))
).order_by('-cantidad_mujeres')

for personas in cantidad_de_personas_por_pais:
    print(f'pais: {personas["pais"]} mujeres: {personas["cantidad_mujeres"]} hombres: {personas["cantidad_hombres"]}')

# for personas in cantidad_de_personas_por_comuna:
#     print(f'comuna: {personas["comuna"]} mujeres: {personas["cantidad_mujeres"]} hombres: {personas["cantidad_hombres"]}')