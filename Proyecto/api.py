
import pandas as pd
from sodapy import Socrata
from ui import nombre_departamento, limite_registros 
from tabulate import tabulate

client = Socrata ("www.datos.gov.co", None)

results = client.get ("gt2j-8ykr", departamento_nom = nombre_departamento, limit = limite_registros)

results_df = pd.DataFrame(results)

columnas_deseadas = {'ciudad_municipio_nom': 'CIUDAD', 'departamento_nom': 'DEPARTAMENTO', 'edad': 'EDAD', 'fuente_tipo_contagio': 'FUENTE CONTAGIO', 'estado': 'ESTADO', 'ubicacion': 'UBICACION DEL CASO'}

results_df = results_df[columnas_deseadas.keys()].rename(columns=columnas_deseadas)

results_df = results_df.sort_values(by=['CIUDAD'])

print(tabulate(results_df, headers='keys', tablefmt='outline'))




