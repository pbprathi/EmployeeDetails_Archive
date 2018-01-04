from sqlalchemy import Column,String,Integer,create_engine,func,DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime



SQLALCHEMY_DATABASE_URI="mysql://{username}:{password}@{host}/{databasename}".format(
    username="root",
    password="Lakshmi@123",
    host="localhost",
    databasename="orders")

Base=declarative_base()

class Employee(Base):
    __tablename__='employee'
    id=Column(Integer,primary_key=True)
    employee_name=Column(String(100))
    employee_age=Column(Integer)
    employee_designation=Column(String(100))
    hired_on=Column(DateTime,default=func.now())

class EmpDetails(Base):
    __tablename__='emp_details'
    id=Column(Integer,primary_key=True)
    employee_name=Column(String(100))
    employee_age=Column(Integer)
    employee_designation=Column(String(100))
    hired_on=Column(DateTime,default=func.now())

engine=create_engine(SQLALCHEMY_DATABASE_URI)
Session=sessionmaker()
Session.configure(bind=engine)
Base.metadata.create_all(engine)
empSession=Session()
