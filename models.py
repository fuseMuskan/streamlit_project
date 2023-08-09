import os
import pandas as pd
import uuid

def save_employee(emp_name: str, job: str, dept_name: str) -> bool:
    try:
        if os.path.exists("employees.csv"):
            emp_df = pd.read_csv("employees.csv")
        else:
            emp_df = pd.DataFrame(columns=["emp_no", "emp_name", "job", "dept_no"])

        dept_df =  pd.read_csv("department.csv")

        dept_no = dept_df[dept_df.iloc[:, 0]==dept_name].head(1)["dept_no"].values[0]
        
        new_data = {
                "emp_name": emp_name,
                "job": job,
                "dept_no": dept_no,
                "emp_no": str(uuid.uuid4())
            }

        new_row = pd.DataFrame([new_data])
        emp_df = pd.concat([emp_df, new_row], ignore_index=True)
        emp_df.to_csv("employees.csv", index=False)
        return True
    
    except Exception as e:
        print("An error occurred:", str(e))
        return False

def save_department(dept_name, location):
    try:
        if os.path.exists("department.csv"):
            emp_df = pd.read_csv("department.csv")
        else:
            emp_df = pd.DataFrame(columns=["dept_name", "location", "dept_no"])

        new_data = {
            "dept_name": dept_name,
            "location": location,
            "dept_no": str(uuid.uuid4())
        }
        new_row = pd.DataFrame([new_data])
        emp_df = pd.concat([emp_df, new_row], ignore_index=True)
        emp_df.to_csv("department.csv", index=False)
        return True

    except Exception as e:
        print("An error occurred:", str(e))
        return False

def get_details():
    try:
        emp_df = pd.read_csv(".\employees.csv")
        department_df = pd.read_csv(".\department.csv")
        df = pd.merge(emp_df, department_df,  on='dept_no')
        return df

    except Exception as e:
        print("An error occurred:", str(e))
        return False

def get_departments():
    department_df = pd.read_csv(".\department.csv")
    departments = department_df["dept_name"]
    dept_names = [name for name in departments]
    dept_names = tuple(set(dept_names))
    return dept_names