import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

table = pd.read_csv(r"C:\Users\esdra\OneDrive\Desktop\Aulas-machine-learning-em-python\aulas\credit_data.csv")

#aki, ele ta até o 4, mas não pega a coluna 4, ou seja, ele pega da coluna 1 até a 3, e a coluna 0 é o id, que não tem relevancia para o modelo
x_table= table.iloc[:, 1:4].values

#pega apenas o 4, ou seja, a coluna 4, que é a coluna de inadimplentes, ou seja, o resultado do modelo
y_table = table.iloc[:, 4].values
#se eu printar isso aki, vai aparecer o tipo de dado, ou seja, o tipo do y_table, que é um array
type(y_table)

print(x_table)