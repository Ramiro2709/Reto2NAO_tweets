import pandas as pd
"""
    Utilizando la libreria pandas, se lee el archivo "tweets.json" que contiene los tweets, y evalua que la estructura sea correcta
    Evalua que los campos existen, y que son del tipo correcto:
    * id: int
    * texto: string
    * usuario: string
    * hashtags: list
    * fecha: datetime
    * retweets: int
    * favoritos: int
    TODO Despues de evaluar que la estructura es correcta, guardar los tweets en una base de datos
"""

def leer_json(nombre_archivo:str):
    data_tweets = pd.read_json(nombre_archivo)
    dataframe_tweets = pd.DataFrame(data_tweets)
    
    # Dataframe
    print("> Tweets:")
    print(dataframe_tweets)
    
    # Tipos de datos
    print("> Tipo de datos de los campos:")
    print(dataframe_tweets.dtypes)
    
    # Verifica que los tipos de datos de cada tweet sea correcta
    campo = "id"
    verificar_campo_existe(dataframe_tweets, campo)
    verificar_campo_es_int(dataframe_tweets[campo])
    
    campo = 'texto'
    verificar_campo_existe(dataframe_tweets, campo)
    verificar_campo_es_string(dataframe_tweets[campo])
    
    campo = 'usuario'
    verificar_campo_existe(dataframe_tweets, campo)
    verificar_campo_es_string(dataframe_tweets[campo])
    
    campo = 'hashtags'
    verificar_campo_existe(dataframe_tweets, campo)
    verificar_campo_es_lista(dataframe_tweets[campo])
    
    campo = 'fecha'
    verificar_campo_existe(dataframe_tweets, campo)
    # Convierte el campo 'fecha' a tipo datetime, si no es fecha validad queda como Nan
    dataframe_tweets[campo] = pd.to_datetime(dataframe_tweets[campo], errors='coerce')
    verificar_campo_es_fecha(dataframe_tweets[campo])
    
    campo = "retweets"
    verificar_campo_existe(dataframe_tweets, campo)
    verificar_campo_es_int(dataframe_tweets[campo])
    
    campo = "favoritos"
    verificar_campo_existe(dataframe_tweets, campo)
    verificar_campo_es_int(dataframe_tweets[campo])
    
    print("> Estructura y tipos de datos OK")

def verificar_campo_existe(dataframe_tweets, campo):
    """
        Verifica que existe el campo indicado
    """    
    if campo not in dataframe_tweets.columns:
        raise Exception(f"Error: no se cuentra el campo '{campo}'")

def verificar_campo_es_int(campo_df):
    id_es_int = campo_df.apply(lambda x: isinstance(x, int)).all()
    if not id_es_int:
        raise Exception("Error: campo no es tipo int")

def verificar_campo_es_string(campo_df):
    id_es_str = campo_df.apply(lambda x: isinstance(x, str)).all()
    if not id_es_str:
        raise Exception("Error: campo no es tipo string")

def verificar_campo_es_fecha(campo_df):
    """
        Verifica que todos los campos fecha se pudieron convertir a datetime
    """
    es_fecha = pd.notna(campo_df).all()
    if not es_fecha:
        raise Exception("Error: campo no es tipo fecha")

def verificar_campo_es_lista(campo_df):
    es_lista = campo_df.apply(lambda x: isinstance(x, list)).all()
    if not es_lista:
        raise Exception("Error: campo no es tipo lista")
    
if __name__ == "__main__":
    leer_json("tweets.json")

