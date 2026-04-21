import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from sklearn.preprocessing import LabelEncoder

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


print(xCensus[0])