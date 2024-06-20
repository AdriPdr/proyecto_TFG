#crear stg idioma y habilidad

import pandas as pd
import os


def find_directory(stg_df, directory03, stg):
    if not os.path.exists(directory03): #se crea el directorio si no existe 
        os.makedirs(directory03)
    stg_df.to_csv(directory03+stg, index=False)

directory02 = "./SILVER/L002/ij_L002_"
directory03 = "./SILVER/L003"


#stg_idioma
file_idioma = "br_stg_ofertas_idiomas.csv"
if os.path.exists(directory02+file_idioma):
    br_stg_idiomas_df = pd.read_csv(directory02+file_idioma)
    stg_idioma_df = br_stg_idiomas_df[["idioma_nombre", "idioma_key"]]
    stg_idioma_df = stg_idioma_df.drop_duplicates()
    find_directory(stg_idioma_df, directory03, "/ij_L003_stg_idioma.csv")


#stg_habilidad
file_habilidad = "br_stg_ofertas_habilidades.csv"
if os.path.exists(directory02+file_habilidad):
    br_stg_ofertas_habilidades_df = pd.read_csv(directory02+file_habilidad)
    stg_habilidad_df = br_stg_ofertas_habilidades_df[["habilidad", "habilidad_key"]]
    stg_habilidad_df = stg_habilidad_df.drop_duplicates()
    find_directory(stg_habilidad_df, directory03, "/ij_L003_stg_habilidad.csv") 


