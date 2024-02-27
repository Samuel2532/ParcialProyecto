
import pandas as pd
from sodapy import Socrata

client = Socrata ("www.datos.gov.co", None )

results = client.get ("gt2j -8 ykr", limit = 10 , departamento =
"VALLE")

results_df = pd.DataFrame.from_records(results)



