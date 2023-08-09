import streamlit as st
from models import save_department

def department():
    st.title("Create Department")

    dept_name = st.text_input("Department Name")
    location = st.text_input("Location")

    if st.button("Save"):
        res = save_department(dept_name, location)
        if res:
            st.write("Department Saved.")
        else:
            st.write("File Not Found.")