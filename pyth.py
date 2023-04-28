salary+float(input("enter salary:"))
benefits=float(input("nter benefits:"))


def calculate_gross_salary(salary ,benfits):
    gross_salary=salary+benfits
    return gross_salary

def calculate_nssf(gross_salary):
    nssf_rate=0.06
    max_deductable_nssf=1800
    nssf=min((gross_salary*nssf_rate),max_dedcuctable_nssf)

    return(nssf)

def calculate_nssf():

 def calculate_nhif(salary,benefits):
    salary= float(input("Enter  salary:"))
    benefits= float(input("Enter benefit:"))  
    gross_salary = salary
    if gross_salary<5999:
        nhif=150
    else:
        nhif=1700
    return(nhif)
nhif = calculate_nhif("salary", "benefits")
print("NHIF=",nhif)

salary=float(input("enter salary:"))
benefits=float(input("enter benefits:"))

#1.variables
#2.data strings-lists
#3.operators
#4.boolean
#5.loops-for
#6.functions