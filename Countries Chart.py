import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

df = df.groupby('Country/Region').sum()

df = df.drop(columns=['Lat','Long'])

df_transp = df.T

df_transp.plot(y=['Brazil', 'Sweden','US'], use_index=True, figsize = (16,8), marker = '*')
