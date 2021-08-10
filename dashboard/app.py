import streamlit as st
# importing dependencies here
import pandas as pd
import os
from utils.pandas import request_df

from charts.index import lite_chart 
# importing plotly modules for visualizations
header = st.empty()

df = request_df()
print(df)
st.bar_chart(data=df['species'].value_counts(), use_container_width=True)

lite_chart(df,'body_mass_(g)','holi')


st.vega_lite_chart(df, {
    "mark": "area",
    "transform": [
        {
            "density": "body_mass_(g)",
            "groupby": ["species"],
            "extent": [df["body_mass_(g)"].min(), df["body_mass_(g)"].max()],
        }
    ],
    "encoding": {
        "x": {"field": "value", "type": "quantitative", "title": "title"},
        "y": {"field": "density", "type": "quantitative"},
        "color": {"field": "species", "type": "nominal"}
    }

}, use_container_width=True)


st.line_chart(data=df.filter(['species','flipper_lenght_(g)']), use_container_width=True)

header.title(f"My first Streamlit App")