import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import StandardScaler

table = pd.read_csv(r"C:\Users\esdra\OneDrive\Desktop\Aulas-machine-learning-em-python\aulas\credit_data.csv")


table['age'].fillna(table['age'].mean(), inplace = True)

table.loc[table['age']<0 , 'age'] = 40.92

#aki, ele ta até o 4, mas não pega a coluna 4, ou seja, ele pega da coluna 1 até a 3, e a coluna 0 é o id, que não tem relevancia para o modelo
x_table= table.iloc[:, 1:4].values

#pega apenas o 4, ou seja, a coluna 4, que é a coluna de inadimplentes, ou seja, o resultado do modelo
y_table = table.iloc[:, 4].values
#se eu printar isso aki, vai aparecer o tipo de dado, ou seja, o tipo do y_table, que é um array
type(y_table)

#antes da alteração
mins = x_table[:,0].min(), x_table[:,1].min(),x_table[:,2].min()

maxs =x_table[:,0].max(), x_table[:,1].max(), x_table[:,2].max()


#aplicando padronização (poderia aplicar normalização, mas nesse caso, a padronização é mais indicada, pq dados tem uma grande variação, ou seja, a renda tem uma variação muito grande, e a idade tem uma variação menor, então a padronização é mais indicada para esse caso)
scaler_table = StandardScaler()
x_table = scaler_table.fit_transform(x_table)


#depois da alteração 
mins = x_table[:,0].min(), x_table[:,1].min(),x_table[:,2].min()



#o x é usado para guardar os previsores, ou seja, as colunas 1, 2 e 3, e o y é usado para guardar a classe, ou seja, a coluna 4, que é a coluna de inadimplentes
print(mins)