import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.header("Solar radiation Mesurements for MoonLight Energy Solutions", divider='rainbow')
with st.sidebar:
    st.header("Solar Radiations")
    add_selectbox = st.sidebar.selectbox(
    "Select City to see his solar radiation measurement",
    ("Benin", "Sierra Leone", "Togo")
    )



