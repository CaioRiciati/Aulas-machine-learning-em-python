import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt 
import plotly.express as px
 
tabela = pd.read_csv(r"C:\Users\caio.eariciati\Desktop\Aulas-machine-learning-em-python-main\aulas\credit_data.csv")


loc =tabela.loc[tabela['age']<0]


media = tabela.mean()


vazio= tabela.isnull()
somatorio = vazio.sum()

#ou
#print(tabela.isnull().sum())
falta=tabela.loc[pd.isnull(tabela['age'])]

tabela['age'].fillna(tabela['age'].mean(), inplace=True)

print(tabela.loc[pd.isnull(tabela['age'])])
print(somatorio)




