import streamlit as st
import webbrowser as wb
import pandas as pd

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= 2025]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state.data = df_data
    


st.markdown("# EAFC 25 OFFICIAL DATASET ⚽️")
st.sidebar.markdown("Desenvolvido por Marcus Sales")

btn = st.button("Acesse os dados do EAFC 25")

if(btn == True):
    wb.open_new_tab("https://www.kaggle.com/datasets/nyagami/ea-sports-fc-25-database-ratings-and-stats?resource=download")
