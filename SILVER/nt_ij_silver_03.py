#Transformaciones a las dimensiones(stg) añadiendo claves únicas a cada una

import pandas as pd
import os
import hashlib


def find_directory(stg_df, directory02, stg):
    if not os.path.exists(directory02): #se crea el directorio si no existe 
        os.makedirs(directory02)
    stg_df.to_csv(directory02+stg, index=False)

directory01 = "./SILVER/L001/ij_L001_"
directory02 = "./SILVER/L002"

#stg_categoria
file_categoria = "stg_categoria.csv"
if os.path.exists(directory01+file_categoria):
    stg_categoria_df = pd.read_csv(directory01+file_categoria)
    stg_categoria_df = stg_categoria_df.drop_duplicates() #eliminamos duplicados
    stg_categoria_df['categoria_key'] = stg_categoria_df.apply(lambda record: hashlib.md5((str(record['categoria_nombre']) + str(record['subcategoria_nombre'])).encode()).hexdigest(), axis=1) #hash de la concatenación de las columnas
    find_directory(stg_categoria_df, directory02, "/ij_L002_"+file_categoria)


#stg_estudio
file_estudio = "stg_estudio.csv"
if os.path.exists(directory01+file_estudio):
    stg_estudio_df = pd.read_csv(directory01+file_estudio)
    stg_estudio_df = stg_estudio_df.drop_duplicates() 
    stg_estudio_df['estudio_key'] = stg_estudio_df.apply(lambda record: hashlib.md5((str(record['estudios_nombre'])).encode()).hexdigest(), axis=1)
    find_directory(stg_estudio_df, directory02, "/ij_L002_"+file_estudio)


#stg_territorio
file_territorio = "stg_territorio.csv"
if os.path.exists(directory01+file_territorio):
    stg_territorio_df = pd.read_csv(directory01+file_territorio)
    stg_territorio_df = stg_territorio_df.drop_duplicates() 
    stg_territorio_df['territorio_key'] = stg_territorio_df.apply(lambda record: hashlib.md5((str(record['pais_nombre']) + str(record['provincia_nombre']) + str(record['ciudad_nombre'])).encode()).hexdigest(), axis=1)     
    find_directory(stg_territorio_df, directory02, "/ij_L002_"+file_territorio)


#br_stg_ofertas_idiomas
file_idioma = "br_stg_ofertas_idiomas.csv"
if os.path.exists(directory01+file_idioma):
    br_stg_idiomas_df = pd.read_csv(directory01+file_idioma)
    br_stg_idiomas_df = br_stg_idiomas_df.drop_duplicates()
    br_stg_idiomas_df['idioma_key'] = br_stg_idiomas_df.apply(lambda record: hashlib.md5((str(record['idioma_nombre'])).encode()).hexdigest(), axis=1)
    find_directory(br_stg_idiomas_df, directory02, "/ij_L002_"+file_idioma)    


#br_stg_ofertas_habilidades
file_habilidad = "br_stg_ofertas_habilidades.csv"
if os.path.exists(directory01+file_habilidad):
    br_stg_habilidad_df = pd.read_csv(directory01+file_habilidad)
    br_stg_habilidad_df = br_stg_habilidad_df.drop_duplicates()
    br_stg_habilidad_df['habilidad_key'] = br_stg_habilidad_df.apply(lambda record: hashlib.md5((str(record['habilidad'])).encode()).hexdigest(), axis=1)
    find_directory(br_stg_habilidad_df, directory02, "/ij_L002_"+file_habilidad)


#stg_compania
file_compania = "stg_compania.csv"
if os.path.exists(directory01+file_compania):
    stg_compania_df = pd.read_csv(directory01+file_compania)
    stg_compania_df = stg_compania_df.drop_duplicates()
    stg_compania_df['compania_key'] = stg_compania_df.apply(lambda record: hashlib.md5((str(record['compania_nombre'])).encode()).hexdigest(), axis=1)
    find_directory(stg_compania_df, directory02, "/ij_L002_"+file_compania)