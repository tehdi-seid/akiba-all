print("============== Employee Payslip ===============\n")

employee_name = input("Enter the employee name: ")
basic_salary = float(input("Enter basic salary: "))
transport_allowance = float(input("Enter transport allowance: "))
food_allowanc = float(input("Enter food allowance: "))

gross_salary = basic_salary+transport_allowance+food_allowanc

print("========================================")
print("            EMPLOYEE PAYSLIP            ")
print("========================================")

print(f"Employee name:      {employee_name}")
print(f"Basic Salary:      {basic_salary:,} ETB")
print(f"Transport Allowance:      {transport_allowance:,} ETB")
print(f"Food Allowance:      {food_allowanc:,} ETB")
print("---------------------------------------\n-")

print(f"gross salary {gross_salary:,} ETB")
print("========================================")
