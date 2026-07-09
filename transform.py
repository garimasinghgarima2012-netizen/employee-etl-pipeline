from extract import *
#cleaned text

total_records=len(employee)
def cleaned_text(employee):
    
    if employee["department"]:
        employee["department"]=employee["department"].strip().upper()
    else:
        employee["department"]="general"
        
    employee["email"]=employee["email"].strip().lower()
    employee["name"]=employee["name"].strip().upper()
    
    
#removing duplicates--
def remove_duplicates(employee):
    ids=set()
    unique=[]
    for i in employee:
        if i["id"] not in ids:
           ids.add(i["id"])
           unique.append(i)
    return(unique)
# r=remove_duplicates(employee)
# print(r)

#string to integer--
def sti(employee):
    for i in employee:
        i["salary"]=int(i["salary"])
    return employee

            
import re #regex
#validate emails--
def validate_email(employee):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, employee["email"]):
        employee["valid_email"]= True
    else:
        employee["valid_email"]= False
        
#increment--
def inc_salary(employee):
    employee["old_salary"]=employee["salary"]
    employee["increment"]=employee["salary"]*0.1
    employee["new_salary"]=employee["old_salary"]+ employee["increment"]
    return employee

def high_rating(employee):
    return list(filter(lambda employee: employee["rating"]>=80,employee))

from functools import reduce
def kpi(employee):
    total_increment = sum(emp["increment"] for emp in employee)
    highest_salary=max(i["new_salary"] for i in employee)
    lowest_salary=min(i["new_salary"] for i in employee)
    return {
        "total records": total_records,
        "valid records": len(employee),
        "total increment": total_increment,
        "highest salary": highest_salary,
        "lowest salary":  lowest_salary
        }
