import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='darkgrid')

st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Covid_Dataset")

covid_india = pd.read_csv('covid_data.csv')
covid=covid_india.head(10)
st.table(covid)

covid_india['Date'] = pd.to_datetime(covid_india['Date'])
covid_india['Confirmed'] = covid_india['Confirmed'].astype('int64')

mask_month = (covid_india['Date'] >= '2021-01-01') & (covid_india['Date'] <= '2021-05-28')
filter_covid = covid_india.loc[mask_month]

#plt.figure(figsize=[20,5])
st.subheader("Cases in January to May 2021 - Kelara - India")
sns.scatterplot(x='Date', y= 'Confirmed', data=filter_covid)
st.pyplot()
#plt.title('Cases in January to May 2021 - Kelara - India')

#plt.figure(figsize=[12,8])
st.subheader("Confirmed cases 2020 and 2021 - Kelara - India")
sns.barplot(x=covid_india['Date'].dt.year, y='Confirmed', data=covid_india)
#plt.title('Confirmed cases 2020 and 2021 - Kelara - India')
#plt.xlabel('Year')
st.pyplot()
