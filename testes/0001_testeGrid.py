import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
import sklearn as sk

#quis testar como ficaria um grid com grafico usando muitas dimensoes.



base = pd.read_csv(r"C:\Users\caio.eariciati\Desktop\Aulas-machine-learning-em-python-main\aulas\credit_data.csv")
print(base)

tab =px.scatter_matrix(base, dimensions=['clientid', 'income', 'age', 'loan', 'default'], color='age')
tab.show()