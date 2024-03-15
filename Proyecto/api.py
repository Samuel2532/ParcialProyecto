
import pandas as pd
from sodapy import Socrata
from tabulate import tabulate
import matplotlib.pyplot as plt

def consultar_datos_api():
    
    #Extracción de datos de la página del gobierno

    client = Socrata ("www.datos.gov.co", None)

    results = client.get ("gt2j-8ykr", departamento_nom = 'RISARALDA', limit = 1000)

    results_df = pd.DataFrame(results)

    '''
    #Características del dataframe en crudo
    print("Number of rows::",results_df.shape[0])
    print("Number of columns::",results_df.shape[1] )
    print("Column Names::",results_df.columns.values.tolist())
    print("Column Data Types::\n",results_df.dtypes)
    print("Columns with Missing Values::",results_df.columns[results_df.isnull().any()].tolist())
    print("General Stats::")
    print(results_df.info())
    print("Summary Stats::" )
    print(results_df.describe())
    '''

    '''Filtros del dataframe'''

    '''
    # Muestra unicamente los valores de una columna
    print("Using Column Name::" )
    print(results_df.pais_viajo_1_nom.values)

    # Muestra unicamente los valores de una columna de cierto tipo
    print("Using Column Data Type::" )
    print(results_df.select_dtypes(include=['object']).values[:,0] )

    # Muestra ciertas filas del dataframe
    print("Select Specific row indices::")
    print(results_df.iloc[[10,501,20]] )

    # Elimina ciertas filas del dataframe
    print("Excluding Specific Row indices::" )
    print(results_df.drop([0,1,2], axis=0).head())
    
    # Muestra ciertas filas del dataframe con ciertos parametros
    print("Subsetting based on logical condition(s)::" )
    print(results_df[results_df.pais_viajo_1_nom == 'ECUADOR'].head())

    # Muestra ciertas filas del dataframe desde arriba hacia abajo
    print("Subsetting based on offset from top (bottom)::" )
    print(results_df[100:].head())
    '''
    
    # Convierte los objetos del dataframe a tipos de datos
    results_df['fecha_reporte_web'] = pd.to_datetime(results_df.fecha_reporte_web)
    results_df['id_de_caso'] = pd.to_numeric(results_df.id_de_caso)
    results_df['fecha_de_notificaci_n'] = pd.to_datetime(results_df.fecha_de_notificaci_n)
    results_df['departamento'] = pd.to_numeric(results_df.departamento)
    results_df['ciudad_municipio'] = pd.to_numeric(results_df.ciudad_municipio)
    results_df['edad'] = pd.to_numeric(results_df.edad)
    results_df['unidad_medida'] = pd.to_numeric(results_df.unidad_medida)
    results_df['pais_viajo_1_cod'] = pd.to_numeric(results_df.pais_viajo_1_cod)
    results_df['fecha_inicio_sintomas'] = pd.to_datetime(results_df.fecha_inicio_sintomas)
    results_df['fecha_diagnostico'] = pd.to_datetime(results_df.fecha_diagnostico)
    results_df['fecha_recuperado'] = pd.to_datetime(results_df.fecha_recuperado)
    results_df['fecha_muerte'] = pd.to_datetime(results_df.fecha_muerte)
    results_df['per_etn_'] = pd.to_numeric(results_df.per_etn_)

    # Tipos de datos del dataframe transformados
    print(results_df.dtypes)
    
    
    # Reemplaza los valores nulos del dataframe 
    results_df['pais_viajo_1_nom'].fillna('COLOMBIA',inplace=True)
    results_df['pais_viajo_1_cod'].fillna(1,inplace=True)
    results_df['nom_grupo_'].fillna('No aplica',inplace=True)
    results_df['fecha_muerte'].fillna('Desconocida',inplace=True)
    results_df['fecha_recuperado'].fillna('No aplica',inplace=True)
    results_df['tipo_recuperacion'].fillna('No aplica',inplace=True)

    '''
    # Imprime el dataframe modificado
    print(tabulate(results_df, headers='keys', tablefmt='outline'))

    
    #Características del dataframe modificado
    print("Number of rows::",results_df.shape[0])
    print("Number of columns::",results_df.shape[1] )
    print("Column Names::",results_df.columns.values.tolist())
    print("Column Data Types::\n",results_df.dtypes)
    print("Columns with Missing Values::",results_df.columns[results_df.isnull().any()].tolist())
    print("General Stats::")
    print(results_df.info())
    print("Summary Stats::" )
    print(results_df.describe())
    '''

    results_df.plot.scatter(x='fecha_diagnostico',y='edad')
    plt.title('Fecha diagnostico y edad ')
    plt.show()


consultar_datos_api()


