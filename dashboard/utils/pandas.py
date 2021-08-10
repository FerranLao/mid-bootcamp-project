import pandas as pd
import streamlit as st
from api.index import api_call

@st.cache
def request_df(*args,**kwargs):
    res = api_call(*args,**kwargs)
    if not res:
        return
    df = pd.json_normalize(res)
    return df