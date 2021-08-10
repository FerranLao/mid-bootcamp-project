    
import streamlit as st

def lite_chart(df, col:str, title:str):
    return st.vega_lite_chart(df, {
        "mark": "area",
        "transform": [
            {
                "density": col,
                "groupby": ["species"],
                "extent": [df[col].min(), df[col].max()],
            }
        ],
        "encoding": {
            "x": {"field": "value", "type": "quantitative", "title": title},
            "y": {"field": "density", "type": "quantitative"},
            "color": {"field": "species", "type": "nominal"}
        }

    }, use_container_width=True)