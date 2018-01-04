from datetime import datetime
import csv,EmpObject


def writeToFile(startDate,endDate):
    '''
    Reads the data from Employee table based on the inputs (startDate & endDate), writes to the CSV file.
    '''
    empf=open('Employee_'+ datetime.now().strftime("%y%m%d%H%M%S") + '.csv','w')
    writer=csv.writer(empf)
    writer.writerow(('Employee_Id','Employee_Name','Employee_Age',
    'Employee_Designation','Hired_On'))

    for instance in EmpObject.empSession.query(EmpObject.Employee).filter(EmpObject.Employee.hired_on.between(startDate,endDate)):
        try:
            writer.writerow((instance.id,instance.employee_name,instance.employee_age,instance.employee_designation,instance.hired_on))
        except ValueError as err:
            print('Bad Row : ',instance)
            print('Reason : ',err)
            continue # Skips to the next row
    empf.close()

startDate=input("Enter the Start date : ")
endDate=input("Enter the End date : ")
writeToFile(startDate,endDate)
