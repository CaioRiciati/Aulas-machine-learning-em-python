import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt 
 
tabela = pd.read_csv(r"C:\Users\caio.eariciati\Desktop\ml\credit_data.csv")

print(tabela.describe())

print(tabela[tabela['age']== 18.0])

qmpaga = np.unique(tabela['default'], return_counts = True )
print(qmpaga)


#graf = sb.countplot(x = tabela['default'])
graf2 = plt.hist(x = tabela['age'])

plt.show()
