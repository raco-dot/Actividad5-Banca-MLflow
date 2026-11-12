"""Descarga y prepara UCI Bank Marketing (bank-full.csv)."""
from pathlib import Path
from urllib.request import urlopen
from io import BytesIO
import zipfile
import pandas as pd

URL = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"
COLS = ['age','job','marital','education','default','balance','housing','loan','contact','day','month','campaign','pdays','previous','poutcome','y']

def obtener_dataset(base):
    base=Path(base); raw=base/'datos'/'datos_ini'; raw.mkdir(parents=True,exist_ok=True)
    destino=raw/'bank-full.csv'
    if destino.exists():
        return destino
    try:
        contenido=urlopen(URL,timeout=90).read()
        with zipfile.ZipFile(BytesIO(contenido)) as outer:
            archivo=next(n for n in outer.namelist() if n.endswith('bank.zip'))
            with zipfile.ZipFile(BytesIO(outer.read(archivo))) as inner:
                destino.write_bytes(inner.read('bank-full.csv'))
    except Exception as e:
        raise RuntimeError('No se pudo descargar el dataset UCI. Descarga bank.zip desde https://archive.ics.uci.edu/dataset/222/bank+marketing y coloca bank-full.csv en datos/datos_ini/') from e
    return destino

def preparar(base):
    base=Path(base)
    ruta=obtener_dataset(base)
    df=pd.read_csv(ruta,sep=';')
    if len(df)!=45211 or 'duration' not in df or 'y' not in df:
        raise ValueError('Dataset inesperado: se requiere bank-full.csv original (45211 filas).')
    # duration se excluye porque no se conoce antes de contactar al cliente.
    df=df.drop(columns=['duration'])
    df=df.drop_duplicates().reset_index(drop=True)
    for c in df.select_dtypes(include='object'):
        df[c]=df[c].str.strip().str.lower()
    df['y']=df['y'].map({'yes':1,'no':0})
    if df['y'].isna().any(): raise ValueError('Etiquetas desconocidas')
    df['y']=df['y'].astype(int)
    salida=base/'datos'/'datos_limp'/'bank_marketing_limpio.csv'
    salida.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(salida,index=False)
    return df

if __name__=='__main__':
    print(preparar(Path(__file__).resolve().parents[1]).shape)
