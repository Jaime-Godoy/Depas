import os
import django
from django.db import connection

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlydepas.settings')
django.setup()

def consultar_inmuebles_por_comuna():
    with connection.cursor() as cursor:
        # Ejecutar la consulta SQL
        cursor.execute('''
            SELECT c.nombre AS comuna, i.nombre AS nombre, i.descripcion AS descripcion
            FROM app_inmueble AS i
            INNER JOIN app_comuna AS c ON i.comuna_id = c.id
            ORDER BY c.nombre
        ''')

        # Obtener los resultados de la consulta
        resultados = cursor.fetchall()

    # Escribir los resultados en un archivo de texto
    with open('inmuebles_por_comuna.txt', 'w') as archivo:
        comuna_actual = None
        for comuna, nombre, descripcion in resultados:
            if comuna != comuna_actual:
                archivo.write(f'Comuna: {comuna}\n')
                comuna_actual = comuna
            archivo.write(f'Nombre: {nombre}\n')
            archivo.write(f'Descripción: {descripcion}\n\n')

def consultar_inmuebles_por_region():
    with connection.cursor() as cursor:
        # Ejecutar la consulta SQL
        cursor.execute('''
            SELECT r.nombre AS region, i.nombre AS nombre, i.descripcion AS descripcion
            FROM app_inmueble AS i
            INNER JOIN app_comuna AS c ON i.comuna_id = c.id
            INNER JOIN app_region AS r ON c.region_id = r.id
            ORDER BY r.nombre
        ''')

        # Obtener los resultados de la consulta
        resultados = cursor.fetchall()

    # Escribir los resultados en un archivo de texto
    with open('inmuebles_por_region.txt', 'w') as archivo:
        region_actual = None
        for region, nombre, descripcion in resultados:
            if region != region_actual:
                archivo.write(f'Región: {region}\n')
                region_actual = region
            archivo.write(f'Nombre: {nombre}\n')
            archivo.write(f'Descripción: {descripcion}\n\n')

# Llamar a la función para realizar la consulta y guardar los resultados en el archivo
consultar_inmuebles_por_region()

# Llamar a la función para realizar la consulta y guardar los resultados en el archivo
consultar_inmuebles_por_comuna()
