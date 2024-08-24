import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.markdown(
    """
    <h1 style=' font-size: 20px; font-weight: bold; color: #eb344c;'>Solar Radiation Measurements For MoonLight Energy Solutions</h1>
    """,
    unsafe_allow_html=True
)
with st.sidebar:
    st.header("Solar Radiations")
    selected_country = st.sidebar.selectbox(
    "Select a country",
    ("Benin", "Sierra Leone", "Togo")
    )
st.write(selected_country)
