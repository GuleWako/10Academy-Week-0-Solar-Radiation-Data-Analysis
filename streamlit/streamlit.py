import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
st.title("Steamlit App")
st.write("Hello world")
data=pd.DataFrame(np.random.randn(20,4),
             columns=['A','B','C','D'])
st.line_chart(data)