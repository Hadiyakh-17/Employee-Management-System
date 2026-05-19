class Employee:

    def __init__(self, emp_id, name, department, salary):

        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_employee(self):

        print("\n----- Employee Details -----")
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)


class EmployeeManagementSystem:

    def __init__(self):

        self.employee_list = []

    def add_employee(self):

        print("\n===== Add Employee =====")

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(emp_id, name, department, salary)

        self.employee_list.append(employee)

        print("\nEmployee Added Successfully.")

    def show_employees(self):

        if len(self.employee_list) == 0:

            print("\nNo Employee Records Found.")

        else:

            print("\n===== Employee Records =====")

            for employee in self.employee_list:
                employee.display_employee()

    def search_employee(self):

        search_id = input("\nEnter Employee ID to Search: ")

        found = False

        for employee in self.employee_list:

            if employee.emp_id == search_id:

                print("\nEmployee Found Successfully.")
                employee.display_employee()

                found = True
                break

        if found == False:

            print("\nEmployee Record Not Found.")


system = EmployeeManagementSystem()

while True:

    print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        system.add_employee()

    elif choice == "2":
        system.show_employees()

    elif choice == "3":
        system.search_employee()

    elif choice == "4":
        print("\nSystem Closed.")
        break

    else:
        print("\nInvalid Choice.")

Repository Name:

Employee-Management-System-Python 💻
