import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

census = pd.read_csv(r"C:\Users\esdra\OneDrive\Desktop\Aulas-machine-learning-em-python\Bases de dados\census.csv")

c2 =census.isnull().sum()

print(np.unique(census['income'], return_counts=True))
sb.countplot( x=census['income'])

#plt.hist(census['age'])
plt.hist(census['education-num'])

grafico2 = px.treemap(census, path=['workclass'])
grafico3 = px.treemap(census, path=['workclass', 'age'])
grafico = px.treemap(census, path=['occupation','income','relationship'])


graf = px.parallel_categories(census, dimensions=['workclass', 'age', 'income'])
graf.show()