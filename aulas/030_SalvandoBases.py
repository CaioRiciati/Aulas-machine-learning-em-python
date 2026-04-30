from sklearn.model_selection import train_test_split
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
import pickle as pk

table =  pd.read_csv(r"C:\Users\caio.eariciati\Desktop\Aulas-machine-learning-em-python-main\aulas\credit_data.csv")



#acho a media e substituo os negativos pela media
media = table.loc[table['age']> 0, 'age'].mean()
table.loc[table['age']<0, 'age'] = media


#preenncho os vazios pela media
table['age'] = table['age'].fillna(table['age'].mean())








#separando previsores 
xcredit = table.iloc[:,1:4].to_numpy()
ycredit = table.iloc[:,4].to_numpy()

xCreditTrei, xCreditTest, yCreditTrei, yCreditTest = train_test_split(xcredit, ycredit , test_size = 0.25, random_state = 0)

print(xCreditTest.shape)

#salvando as bases de dados de treinamentos e teste com o preprocessamento já aplicado
#agora qnd eu for trabalhar com algoritimos, eu só preciso carregar os arquivos ao inves de fazer toda essa limpeza e processamento dos dados dnv
with open('credit.pkl', mode = 'wb') as f:
    pk.dump([xCreditTrei, yCreditTrei,xCreditTest,yCreditTest], f)