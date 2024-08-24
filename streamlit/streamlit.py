import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Function to read data from a CSV file based on country name
def readData(data):
    if data=='Benin':
        return 'data/benin-malanville.csv'
    elif data=='Sierra Leone':
        return 'data/sierraleone-bumbuna.csv'
    elif data =='Togo':
        return 'data/togo-dapaong_qc.csv'
    else:
        print("No data with this name")

# Function to create a box plot for identifying outliers
def boxPlotForIdentifyOutlier(data,ax):
    sns.boxplot(data=data[['DNI', 'GHI', 'DHI']], orient='v')
    plt.title('Box Plot of Solar Radiation Data')
    plt.xlabel('Values')
    plt.ylabel('Solar Radiation Type')
    plt.show()

# Function to check for outliers and negative values in a specific column
def CheckOutLiersAndNegativeValue(data, column_name):
    # Calculate quartiles and IQR
    q1 = data[column_name].quantile(0.25)
    q3 = data[column_name].quantile(0.75)
    iqr = q3 - q1

     # Calculate lower and upper bounds
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    # Find outliers and negative values
    outliers = data[(data[column_name] < lower_bound) | (data[column_name] > upper_bound)]
    negativeValue = data[data[column_name] <0]
    print(f"Outliers in {column_name}: {outliers.shape[0]} Negative value in  {column_name}: {negativeValue.shape[0]}")

# Function to replace negative values with zeros
def replaceNegativeWithZero(data, column_names):
    for column_name in column_names:
        data[column_name] = data[column_name].clip(lower=0)
    return data

# Function to remove outliers using winsorization
def removeOutliersWinsorization(data, column_names,):
    for column_name in column_names:
        q1 = data[column_name].quantile(0.25)
        q3 = data[column_name].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        data[column_name] = data[column_name].clip(lower_bound, upper_bound)
    return data;

# Function to plot solar radiation data over time
def solarRadiationsOvertime(data):
    # Plot GHI, DNI, and DHI over time
    plt.figure(figsize=(12, 6))
    plt.plot(data['Timestamp'], data['GHI'])
    plt.plot(data['Timestamp'], data['DNI'])
    plt.plot(data['Timestamp'], data['DHI'])
    plt.title('Solar Radiation Over Time')
    plt.ylabel('Solar Radiations')
    plt.xlabel('Timestamp')
    plt.legend(['GHI','DNI','DHI'])
    plt.show()

# Function to evaluate the impact of cleaning on solar radiation data
def evaluateImpactofCleaningOvertime(cleaned_data,uncleaned_data):
    plt.figure(figsize=(12, 6))
    plt.plot(uncleaned_data['Timestamp'], uncleaned_data['ModA'], label='Uncleaned ModA')
    plt.plot(uncleaned_data['Timestamp'], uncleaned_data['ModB'], label='Uncleaned ModB')
    plt.plot(cleaned_data['Timestamp'], cleaned_data['ModA'], label='Cleaned ModA')
    plt.plot(cleaned_data['Timestamp'], cleaned_data['ModB'], label='Cleaned ModB')
    plt.title('ModA Readings Before and After Cleaning')
    plt.xlabel('Timestamp')
    plt.ylabel('ModA Value')
    plt.legend()
    plt.show()

# Function to analyze the correlation between solar radiation and temperature
def correlationBetweenSolarRadiationandTemperature(data):
    correlation_matrix = data[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

# Function to analyze wind speed and direction using a polar plot(same with scatter plot)
def correlationBetweenSolarRadiationandWind(data):
    sns.pairplot(data[['GHI', 'DNI', 'DHI', 'WS', 'WSgust', 'WD']])
    plt.show()

# Function to analyze wind speed and direction using a polar plot
def windAnalysiswithWindspeedAndWindDirection(data):
    wind_speed = data['WS']
    wind_direction_degrees = data['WD']
    wind_direction_radians = np.radians(wind_direction_degrees)
    plt.figure(figsize=(6, 6))
    plt.polar(wind_direction_radians, wind_speed,marker='o', linestyle='', label='Wind Data')
    plt.title('Wind Speed and Direction')
    plt.xlabel('Wind Direction (radians)')
    plt.ylabel('Wind Speed (m/s)')
    plt.grid(True)
    plt.show()

# Function to analyze the influence of relative humidity on temperature and solar radiation
def examineRelativeHumidityInfluenceTempAndSolarRadiation(data):
    correlation_matrix = data[['RH', 'TModA', 'TModB', 'GHI', 'DNI', 'DHI']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

# Function to create histograms for solar radiation, wind speed, and temperature
def freqDesForSolarRadWSandTempUsingHistogram(data):
    plt.figure(figsize=(15, 10))
    plt.subplot(3, 2, 1)
    plt.hist(data['GHI'], bins=30, color='blue')
    plt.title('GHI Histogram')
    plt.xlabel('GHI (W/m²)')
    plt.ylabel('Frequency')

    plt.subplot(3, 2, 2)
    plt.hist(data['DNI'], bins=30, color='orange')
    plt.title('DNI Histogram')
    plt.xlabel('DNI (W/m²)')
    plt.ylabel('Frequency')

    plt.figure(figsize=(15, 10))
    plt.subplot(3, 2, 3)
    plt.hist(data['DHI'], bins=30, color='green')
    plt.title('DHI Histogram')
    plt.xlabel('DHI (W/m²)')
    plt.ylabel('Frequency')

    plt.subplot(3, 2, 4)
    plt.hist(data['WS'], bins=30, color='purple')
    plt.title('WS Histogram')
    plt.xlabel('WS (m/s)')
    plt.ylabel('Frequency')

    plt.subplot(3, 2, 5)
    plt.hist(data['Tamb'], bins=30, color='red')
    plt.title('Tamb Histogram')
    plt.xlabel('Tamb (m/s)')
    plt.ylabel('Frequency')
    # ... continue for DHI, WS, and Tamb

    plt.tight_layout()
    plt.show()


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
st.pyplot(solarRadiationsOvertime(data))


cleaned_data = data[data['Cleaning'] == 1]
uncleaned_data = data[data['Cleaning'] == 0]
st.header("Cleaned Data")
st.divider()
st.write(cleaned_data.head())

st.header("Impact of Cleaning data overTime")
st.divider()
st.pyplot(evaluateImpactofCleaningOvertime(cleaned_data, uncleaned_data))


st.header("Correlation Between Solar Radiation and Temperature")
st.divider()
st.pyplot(correlationBetweenSolarRadiationandTemperature(data))

st.header("Correlation Between Solar Radiation and Winds")
st.divider()
st.pyplot(correlationBetweenSolarRadiationandWind(data))

st.header("Wind Analysis With Wind Speed And Wind Direction")
st.divider()
st.pyplot(windAnalysiswithWindspeedAndWindDirection(data))

st.header("Relative Humidity Influence Temp and Solar Radiation")
st.divider()
st.pyplot(examineRelativeHumidityInfluenceTempAndSolarRadiation(data))


st.header("Frequency distribution of Solar Radiation, wind speed and Temp")
st.divider()
st.pyplot(freqDesForSolarRadWSandTempUsingHistogram(data))
