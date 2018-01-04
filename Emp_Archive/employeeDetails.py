import os,EmpObject

def createEmployees():
    noOfEmployees=int(input('Enter the No of employees : '))
    for i in range(noOfEmployees):
        employee_Name=input('Enter the {} Employee_Name : '.format(i))
        employee_Age=input('Enter tehe Employee_Age : ')
        employee_Designation=input('Enter the Employee_Designation : ')
        new_Record=EmpObject.Employee(employee_name=employee_Name,employee_age=employee_Age,employee_designation=employee_Designation)
        EmpObject.empSession=session()
        EmpObject.empSession.add(new_Record)
        EmpObject.empSession.commit()

createEmployees()
