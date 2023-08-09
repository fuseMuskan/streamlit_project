import streamlit as st
from employee import employee
from department import department
from details import details_page

page_names_to_funcs = {
    "Department": department,
    "Employee": employee,
    "Details": details_page
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
