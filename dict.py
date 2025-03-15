# Creating a nested dictionary (dictionary inside a dictionary)
company_info = {
    "company_name": "TechCorp",
    "employees": {
        "001": {"name": "INOOL", "role": "Developer", "salary": 70000},
        "002": {"name": "DD", "role": "Designer", "salary": 60000},
        "003": {"name": "ASIKA", "role": "Manager", "salary": 90000}
    },
    "location": "New York"
}

# Accessing nested dictionary values
employee_id = "001"
print(f"Employee {employee_id} Name:", company_info["employees"][employee_id]["name"])
print(f"Employee {employee_id} Role:", company_info["employees"][employee_id]["role"])
print(f"Employee {employee_id} Salary:", company_info["employees"][employee_id]["salary"])

# Modifying a nested value
company_info["employees"]["003"]["salary"] = 95000
print("\nUpdated Salary for ASIKA:", company_info["employees"]["003"]["salary"])

# Adding a new employee
company_info["employees"]["004"] = {"name": "Iswarya", "role": "HR", "salary":80000}
print("\nNew Employee Added:", company_info["employees"]["004"])
