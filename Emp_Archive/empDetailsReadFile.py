import csv,os,shutil,glob,EmpObject

def writeToDb(filename,*,errors='warn'):
    '''
    Reads the data from Employee_Datetime.csv file and inserts to the Emp_details table.
    '''
    if errors not in ('warn','silent','raise'):
        raise ValueError("Errors must have one of 'warn','silent','raise'")
    with open(name,'r') as rf:
        rows=csv.reader(rf)
        headers=next(rows) #skip the header row
        result="Success"
        for row in rows:
            try:
                new_Record=EmpObject.EmpDetails(id=row[0],employee_name=row[1],
                employee_age=row[2],employee_designation=row[3],
                hired_on=row[4])
                EmpObject.empSession.add(new_Record)
                EmpObject.empSession.commit()
            except ValueError as err:
                if errors=='warn':
                    print('Bad Row : ',row)
                    print('Reason : ',err)
                    result="Error"
                elif errors=='raise':
                    raise
                else:
                    pass
                continue # skips to the next row
    return result

cwd=os.getcwd()
for name in glob.glob('*.csv'):
    try:
        result=writeToDb(name,errors='warn')
        if result=="Success":
            shutil.move(cwd + '/' + name, cwd +'/archive')
            #os.rename(cwd + '/' + name, cwd +'/archive')
        print(result)
    except Exception as e:
        print('Exception : ',name)
        print('Reason : ',e)
        continue # skips to the next file
