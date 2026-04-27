import pandas as pd
import numpy as np
import random

np.random.seed(42)

n = 1200  


sexos = ['M', 'F']
planos = ['Basico', 'Intermediario', 'Premium']
uso_app = ['Sim', 'Nao']

data = []

for _ in range(n):
    idade = np.random.randint(18, 65)
    sexo = random.choice(sexos)
    tempo_cliente = np.random.randint(1, 60)
    plano = random.choice(planos)
    
    # valor depende do plano
    if plano == 'Basico':
        valor = np.random.normal(30, 5)
    elif plano == 'Intermediario':
        valor = np.random.normal(55, 10)
    else:
        valor = np.random.normal(90, 15)

    numero_suporte = np.random.poisson(2)
    usa_app = random.choice(uso_app)

    # regra de churn (com lógica + ruído)
    churn_prob = 0.2
    if plano == 'Basico':
        churn_prob += 0.2
    if numero_suporte > 3:
        churn_prob += 0.2
    if usa_app == 'Nao':
        churn_prob += 0.2
    if tempo_cliente < 6:
        churn_prob += 0.2

    churn = 1 if np.random.rand() < churn_prob else 0

    data.append([
        idade, sexo, tempo_cliente, plano,
        round(valor, 2), numero_suporte, usa_app, churn
    ])

df = pd.DataFrame(data, columns=[
    'idade', 'sexo', 'tempo_cliente', 'plano',
    'valor_mensal', 'numero_suporte', 'usa_app', 'churn'
])

df.insert(0, 'id_cliente', range(1, len(df) + 1))

#  ADICIONANDO RUÍDO



for col in ['idade', 'sexo', 'numero_suporte']:
    df.loc[df.sample(frac=0.05).index, col] = np.nan




df.loc[df.sample(frac=0.05).index, 'usa_app'] = 'nao'
df.loc[df.sample(frac=0.03).index, 'sexo'] = ' F'

# outliers
df.loc[df.sample(frac=0.02).index, 'valor_mensal'] = 999

# valores inválidos
df.loc[df.sample(frac=0.01).index, 'tempo_cliente'] = -5
df.loc[df.sample(frac=0.01).index, 'valor_mensal'] = 'erro'

# salvar
df.to_csv('churn_clientes_1200_linhas.csv', index=False)

print("Dataset gerado com sucesso!")