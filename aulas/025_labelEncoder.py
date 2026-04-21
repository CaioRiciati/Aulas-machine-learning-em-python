import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

census = pd.read_csv(r"Bases de dados/census.csv")
xCensus = census.iloc[:, 0:14].to_numpy()
yCensus = census.iloc[:, 14].to_numpy()

workclass = LabelEncoder()
education = LabelEncoder()
martial_status = LabelEncoder()
occupation = LabelEncoder()
relationship = LabelEncoder()
race = LabelEncoder()
sex = LabelEncoder()
nativeCountry = LabelEncoder()


xCensus[:,1] = workclass.fit_transform(xCensus[:,1])
xCensus[:,3] = education.fit_transform(xCensus[:,3])
xCensus[:,5] = martial_status.fit_transform(xCensus[:,5])
xCensus[:,6] = occupation.fit_transform(xCensus[:,6])
xCensus[:,7] = relationship.fit_transform(xCensus[:,7])
xCensus[:,8] = race.fit_transform(xCensus[:,8])
xCensus[:,9] =sex.fit_transform(xCensus[:,9])
xCensus[:,13] = nativeCountry.fit_transform(xCensus[:,13])




onehotencoder = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [1,3,5,6,7,8,9,13])] , remainder ='passthrough')


xCensus = onehotencoder.fit_transform(xCensus).toarray()


#fazendo o escalonamento dos dados
scalerCensus = StandardScaler()
xCensus = scalerCensus.fit_transform(xCensus)



print(xCensus[0])




#p contar qnts atributos categoricos tem cada coluna(aki no caso é na colina workclass)
len(np.unique(census['workclass']))