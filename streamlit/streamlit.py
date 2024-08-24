import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

import sys
sys.path.append('..')
from scripts.solarRadiationData import readData,boxPlotForIdentifyOutlier,replaceNegativeWithZero,removeOutliersWinsorization,solarRadiationsOvertime


st.markdown(
    """
    <h1 style=' font-size: 40px; text-align:center; font-weight: bold; color: #eb344c;'>Analysis Solar Radiation Measurement of MoonLight Energy Solutions</h1>
    """,
    unsafe_allow_html=True
)
with st.sidebar:
    st.header("Solar Radiations")
    selected_country = st.sidebar.selectbox(
    "Select a country",
    ("Benin", "Sierra Leone", "Togo")
    )
if selected_country =='Benin':
    st.text(body="Solar Radiation Measurement Data of Benin")
elif selected_country =='Sierra Leone':
    st.text("Solar Radiation Measurement Data of Sierra Leone")
else:
    st.text("Solar Radiation Measurement Data of Togo")

#read data
data = pd.read_csv(readData(selected_country))
st.header("Data before Cleaning and Pre-processing")
st.divider()
st.dataframe(data.head())


data=data.drop('Comments',axis=1)
st.header("Drop the Null columns")
st.divider()
st.dataframe(data.head())

st.header("Summary Statistics of "+selected_country +" Data")
st.divider()
st.dataframe(data.describe())


st.header("Box-plot Of Solar Radiation With Outliers")
st.divider()
fig, ax = plt.subplots()
# Call your box plot function and pass the axis to it
boxPlotForIdentifyOutlier(data,ax)
# Display the plot in Streamlit
st.pyplot(fig)

data= replaceNegativeWithZero(data,['DNI','GHI','DHI'])
st.header("Remove Negative Value Of Solar Radiation")
st.text(body="Replace all negative value with zero")
st.divider()
st.write(data.describe())

data= removeOutliersWinsorization(data,['DNI','GHI','DHI','ModA','ModB','WS','WSgust'])
st.header("Remove Outliers Using Winsorization")
st.text(body="Replace lower cutoff point with the lower value, and replace upper cutoff point with the upper value")
st.divider()
st.write(data.describe())

st.header("Box-plot Of Solar Radiation With-out Outliers")
st.divider()
fig, ax = plt.subplots()
boxPlotForIdentifyOutlier(data,ax)
st.pyplot(fig)

st.header("Time Series Analysis of Solar Radiation")
st.divider()
# st.pyplot(solarRadiationsOvertime(data))


cleaned_data = data[data['Cleaning'] == 1]
uncleaned_data = data[data['Cleaning'] == 0]
st.header("Cleaned Data")
st.divider()
st.write(cleaned_data.head())
