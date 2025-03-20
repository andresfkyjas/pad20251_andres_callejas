import requests
import json
import pandas as pd

class Transformation:
    def __init__(self):
        self.ruta_static = "src/ibgd/static/"

    
    def dataset_1(self):
        df_1= pd.DataFrame()
        print("se genero df 1")
        return df_1

    def dataset_2(self):
        df_2= pd.DataFrame()
        print("se genero df 2")
        return df_2

    def join_dataset(self,df_1=pd.DataFrame(),df_2=pd.DataFrame(),nom_col1="",nom_col2=""):
        df_3= pd.DataFrame()
        print("se genero df 3")
        return df_3
    
    def auditoria(self,df=pd.DataFrame()):
        print("se genero df autoria")
        return True

    def ejecucion(self):
        df1 =self.dataset_1()
        df2 = self.dataset_1()
        df3 = self.dataset_1(df1,df2)
        if self.auditoria(df3):
            print("Termino actividad 3")

trx = Transformation()
trx.ejecucion()