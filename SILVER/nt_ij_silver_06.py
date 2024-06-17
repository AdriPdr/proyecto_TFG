#Crear las dimensiones correspondientes y la tabla de hechos de las ofertas

import pandas as pd
import os

def find_directory(stg_df, directory, stg): 
    if not (os.path.exists(directory)):
        os.makedirs(directory)
    stg_df.to_csv(directory+stg, index=False)


directory_read_L002 = "C:/Users/apedr/OneDrive/Escritorio/proyecto_TFG/SILVER/L002/ij_L002_"
directory_read_L003 = "C:/Users/apedr/OneDrive/Escritorio/proyecto_TFG/SILVER/L003/ij_L003_"
directory_read_L004 = "C:/Users/apedr/OneDrive/Escritorio/proyecto_TFG/SILVER/L004/ij_L004_"
directory_load = "C:/Users/apedr/OneDrive/Escritorio/proyecto_TFG/GOLD/"

#dim_categoria
if (os.path.exists(directory_read_L002+"stg_categoria.csv")): 
    stg_categoria_df = pd.read_csv(directory_read_L002+"stg_categoria.csv")
    find_directory(stg_categoria_df, directory_load, "dim_categoria.csv")

#dim_estudio
if (os.path.exists(directory_read_L002+"stg_estudio.csv")): 
    stg_estudio_df = pd.read_csv(directory_read_L002+"stg_estudio.csv")
    find_directory(stg_estudio_df, directory_load, "dim_estudio.csv")

#dim_territorio
if (os.path.exists(directory_read_L002+"stg_territorio.csv")): 
    stg_territorio_df = pd.read_csv(directory_read_L002+"stg_territorio.csv")
    find_directory(stg_territorio_df, directory_load, "dim_territorio.csv")

#br_stg_habilidades
if (os.path.exists(directory_read_L002+"br_stg_ofertas_habilidades.csv")): 
    br_stg_habilidades = pd.read_csv(directory_read_L002+"br_stg_ofertas_habilidades.csv")
    find_directory(br_stg_habilidades, directory_load, "br_dim_ofertas_habilidades.csv")

#br_stg_idiomas
if (os.path.exists(directory_read_L002+"br_stg_ofertas_idiomas.csv")): 
    br_stg_idiomas = pd.read_csv(directory_read_L002+"br_stg_ofertas_idiomas.csv")
    find_directory(br_stg_idiomas, directory_load, "br_dim_ofertas_idiomas.csv")

#stg_habilidad
if (os.path.exists(directory_read_L003+"stg_habilidad.csv")): 
    stg_habilidad_df = pd.read_csv(directory_read_L003+"stg_habilidad.csv")
    find_directory(stg_habilidad_df, directory_load, "dim_habilidad.csv")

#stg_idioma
if (os.path.exists(directory_read_L003+"stg_idioma.csv")): 
    stg_idioma_df = pd.read_csv(directory_read_L003+"stg_idioma.csv")
    find_directory(stg_idioma_df, directory_load, "dim_idioma.csv")

#stg_compania
if (os.path.exists(directory_read_L002+"stg_compania.csv")): 
    stg_compania_df = pd.read_csv(directory_read_L002+"stg_compania.csv")
    find_directory(stg_compania_df, directory_load, "dim_compania.csv")

#wide_table_ofertas
if (os.path.exists(directory_read_L004+"wide_table_ofertas.csv")): 
    wide_table_df = pd.read_csv(directory_read_L004+"wide_table_ofertas.csv")
    find_directory(wide_table_df, directory_load, "ij_fact_ofertas.csv")