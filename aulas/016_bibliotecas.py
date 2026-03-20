import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

basec = pd.read_csv(r"C:\Users\esdra\OneDrive\Desktop\Aulas-machine-learning-em-python\aulas\credit_data.csv")
print(basec.head())
print(basec.describe())