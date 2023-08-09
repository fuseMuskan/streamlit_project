import streamlit as st
from models import get_details

def details_page():
    st.title("Details Page")
    df = get_details()
    st.table(data= df)




