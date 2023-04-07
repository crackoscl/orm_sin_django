
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
url = BASE_DIR / 'datos' / 'permanencias_definitivas_otorgadas_2000_al_2011.xlsx'
url_csv = BASE_DIR / 'datos' / 'permanencias_definitivas_otorgadas_2000_al_2011.csv'

read_file = pd.read_excel(url)
read_file.to_csv(url_csv,index=None,header=True)