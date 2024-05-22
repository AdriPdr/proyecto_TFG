# Creación de dimensiones (stg)

import pandas as pd
import os

def find_directory(stg_df, directory, stg):
    if not os.path.exists(directory): #se crea el directorio si no existe 
        os.makedirs(directory)
    stg_df.to_csv(directory+stg, index=False)
    
file_path = "C:/Users/apedr/OneDrive/Escritorio/proyecto_TFG/SILVER/L000/ij_L000_wide_table_ofertas.csv"

if os.path.exists(file_path):
    info_infoJobs_df =pd.read_csv(file_path)
    directory = "C:/Users/apedr/OneDrive/Escritorio/proyecto_TFG/SILVER/L001"

    #stg_categoria
    ij_stg_categoria_df = info_infoJobs_df[["categoria_nombre", "subcategoria_nombre"]] 
    stg = "/ij_L001_stg_categoria.csv"
    find_directory(ij_stg_categoria_df, directory, stg)


    #stg_estudio
    ij_stg_estudios_df = info_infoJobs_df[["estudios_nombre"]]
    stg = "/ij_L001_stg_estudio.csv"
    find_directory(ij_stg_estudios_df, directory, stg)


    #br_stg_ofertas_habilidades
    ij_br_stg_ofertas_habilidades_df = info_infoJobs_df[["oferta_id", "habilidad"]]
    stg = "/ij_L001_br_stg_ofertas_habilidades.csv"
    find_directory(ij_br_stg_ofertas_habilidades_df, directory, stg)


    #br_stg_ofertas_idiomas
    ij_br_stg_ofertas_idiomas_df = info_infoJobs_df[["oferta_id", "idioma_nombre"]]
    stg = "/ij_L001_br_stg_ofertas_idiomas.csv"
    find_directory(ij_br_stg_ofertas_idiomas_df, directory, stg)


    #stg_territorio
    ij_stg_territorio_df = info_infoJobs_df[["pais_nombre", "provincia_nombre", "ciudad_nombre"]]
    stg = "/ij_L001_stg_territorio.csv"
    find_directory(ij_stg_territorio_df, directory, stg)


    #stg_compania
    ij_stg_compania_df = info_infoJobs_df[["oferta_id", "compania_nombre"]]
    stg = "/ij_L001_stg_compania.csv"
    find_directory(ij_stg_compania_df, directory, stg)

