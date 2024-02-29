import pandas as pd
from tabulate import tabulate

# Datos proporcionados
datos = [{'fecha_reporte_web': '2020-08-05 00:00:00', 'id_de_caso': '337095', 'fecha_de_notificaci_n': '2020-07-10 00:00:00', 'departamento': '91', 'departamento_nom': 'AMAZONAS', 'ciudad_municipio': '91001', 'ciudad_municipio_nom': 'LETICIA', 'edad': '22', 'unidad_medida': '1', 'sexo': 'F', 'fuente_tipo_contagio': 'Comunitaria', 'ubicacion': 'Casa', 'estado': 'Leve', 'recuperado': 'Recuperado', 'fecha_inicio_sintomas': '2020-07-10 00:00:00', 'fecha_diagnostico': '2020-08-04 00:00:00', 'fecha_recuperado': '2020-08-10 00:00:00', 'tipo_recuperacion': 'PCR', 'per_etn_': '1', 'nom_grupo_': 'Por definir'}]

# Convertir los datos a un DataFrame de Pandas
df = pd.DataFrame(datos)

# Seleccionar solo las columnas deseadas y renombrar las columnas
columnas_deseadas = {'ciudad_municipio_nom': 'Ciudad', 'departamento_nom': 'Departamento', 'edad': 'Edad', 'fuente_tipo_contagio': 'Tipo', 'estado': 'Estado', 'nom_grupo_': 'País de procedencia'}
df = df[columnas_deseadas.keys()].rename(columns=columnas_deseadas)

# Ordenar los datos por columnas (en este caso, por 'Ciudad')
df = df.sort_values(by=['Ciudad'])

# Imprimir el DataFrame con formato tabular
print(tabulate(df, headers='keys', tablefmt='pretty'))