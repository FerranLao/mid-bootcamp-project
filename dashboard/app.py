import streamlit as st
# importing dependencies here
import pandas as pd
import os
# importing plotly modules for visualizations
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode, iplot
header = st.empty()

df = pd.read_csv('./penguins.csv')

st.vega_lite_chart(df, {
    "mark": "area",
    "transform": [
        {
            "density": "Body Mass (g)",
            "groupby": ["Species"],
            "extent": [df["Body Mass (g)"].min(), df["Body Mass (g)"].max()],
        }
    ],
    "encoding": {
        "x": {"field": "value", "type": "quantitative", "title": "title"},
        "y": {"field": "density", "type": "quantitative"},
        "color": {"field": "Species", "type": "nominal"}
    }

}, use_container_width=True)

header.title(f"My first Streamlit App")