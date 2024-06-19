#Transformar algunos tipos de datos de la tabla ancha

import pandas as pd
import os


file_path = "./BRONZE/infoInfojobs.csv"

if os.path.exists(file_path): 
    info_infoJobs_df = pd.read_csv(file_path) 

    directory = "./SILVER/L000"

    info_infoJobs_df["aplicaciones"] = info_infoJobs_df["aplicaciones"].astype("Int64")
    info_infoJobs_df["salario_maximo"] = info_infoJobs_df["salario_maximo"].astype(float)
    info_infoJobs_df["salario_minimo"] = info_infoJobs_df["salario_minimo"].astype(float)
    info_infoJobs_df["vacantes"] = info_infoJobs_df["vacantes"].astype("Int64")

    if not os.path.exists(directory): #se crea el directorio si no existe 
        os.makedirs(directory)


    info_infoJobs_df.to_csv(directory+"/ij_L000_wide_table_ofertas.csv")


