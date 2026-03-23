import pandas as pd
import seaborn as sb
 
tabela = pd.read_csv(r"C:\Users\caio.eariciati\Desktop\ml\credit_data.csv")

print(tabela.describe())

vazio = ()

print(tabela[tabela['age']== vazio])

