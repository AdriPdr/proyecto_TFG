#Creación final de la tabla ancha

import pandas as pd
import os

def find_directory(stg_df, directory, stg):
    if not os.path.exists(directory): #se crea el directorio si no existe 
        os.makedirs(directory)
    stg_df.to_csv(directory+stg, index=False)

directory_fact = "./SILVER/L000/ij_L000_wide_table_ofertas.csv"
directory_stg = "./SILVER/L002/ij_L002_"
directory_stg2 = "./SILVER/L003/ij_L003_"
directory = "./SILVER/L004"

if(os.path.exists(directory_fact)):
    ft_ij_df = pd.read_csv(directory_fact)
    if(os.path.exists(directory_stg+"stg_categoria.csv")):
        #join con categoria
        stg_categoria_df = pd.read_csv(directory_stg+"stg_categoria.csv")
        joined_df = pd.merge(ft_ij_df, stg_categoria_df, on=['categoria_nombre', 'subcategoria_nombre'])

        #join con estudio
        if(os.path.exists(directory_stg+"stg_estudio.csv")):
            stg_estudio_df = pd.read_csv(directory_stg+"stg_estudio.csv")
            joined_df = pd.merge(joined_df, stg_estudio_df, on=['estudios_nombre']) 

            #stg_territorio
            if(os.path.exists(directory_stg+"stg_territorio.csv")):
                stg_territorio_df = pd.read_csv(directory_stg+"stg_territorio.csv")
                joined_df = pd.merge(joined_df, stg_territorio_df, on=['pais_nombre', 'provincia_nombre', 'ciudad_nombre'], how='left')

                #stg_compania
                if(os.path.exists(directory_stg+"stg_compania.csv")):
                    stg_compania_df = pd.read_csv(directory_stg+"stg_compania.csv")
                    joined_df = pd.merge(joined_df, stg_compania_df, on=['compania_nombre'], how='left')  

                    joined_df = joined_df[['oferta_id', 'titulo', 'aplicaciones', 'descripcion', 'experiencia_minima', 'jornada_laboral', 'link',
                                            'requisitos_minimos', 'salario_descripcion', 'salario_maximo', 'salario_minimo', 'vacantes',
                                            'categoria_key', 'estudio_key', 'territorio_key', 'compania_key', 'creationDate']]
                    joined_df = joined_df.drop_duplicates()
                    find_directory(joined_df, directory, "/ij_L004_wide_table_ofertas.csv")

                    