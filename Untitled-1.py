def calculate_nhif(salary,benefits):
    salary= float(input("Enter  salary:"))
    benefits= float(input("Enter benefit:"))  
    gross_salary = salary
    if gross_salary<5999:
        nhif=150
    else:
        nhif=0

    return(nhif)
nhif=calculate_nhif ("salary,"benefits")
print("NHIF="nhif)


