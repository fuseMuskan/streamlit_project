import streamlit as st
from models import save_employee, get_departments

def employee():
    st.title("Create Employee")
    departments = get_departments()
    emp_name = st.text_input("Employee Name")
    job = st.text_input("Job")
    dept_name = st.selectbox("Department Name",
                            departments)

    if st.button("Save"):
        res = save_employee(emp_name, job, dept_name)
        if res:
            st.write("Employee Saved.")
        else:
            st.write("File Not Found.")



