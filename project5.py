print("--- Pyhton Employee Management System ---\n")

person = None
employee = None
manager = None

while True:

    print("Choose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show details")
    print("5. Exit\n")

    choice = int(input("Enter your choice: "))
    print()

    match choice:
        case 1:
            class Person:
                def __init__(self):
                    self.name = input("Enter Name: ")
                    self.age = int(input("Enter Age: "))

                    print(f"Person created with name: {self.name} and age: {self.age}.\n")
                    print("--- Choose another operation ---\n")

                def __del__(self):
                    print("Person object deleted.")
                
            person = Person()

        case 2:
            class Employee:

                def __init__(self):
                    self.em_name = input("Enter Name: ")
                    self.em_age = int(input("Enter Age: "))
                    self.__em_id = input("Enter Employee ID: ")
                    self.__em_sal = int(input("Enter Employee Salary: "))
                    print()

                    print(
                        f"Employee created with name: {self.em_name}, "
                        f"age: {self.em_age}, "
                        f"ID: {self.get_id()} "
                        f"and salary: ${self.get_salary()}."
                    )
                    print()

                def get_id(self):
                    return self.__em_id

                def get_salary(self):
                    return self.__em_sal
                
            employee = Employee()

            print("--- Choose another operation ---\n")

        case 3:
            class Manager(Employee):
                def __init__(self):
                    super().__init__()
                    self.dep = input("Enter Department: ")
                    print()

                    print(f"Manager created with name: {self.em_name}, age: {self.em_age}, ID: {self.get_id()}, salary: ${self.get_salary()} and department: {self.dep}.\n")
            
            manager = Manager()
            
            print("Is Manager a subclass of Employee?", issubclass(Manager, Employee))
            print()
            print("--- Choose another operation ---\n")
        
        case 4:
            print("Choose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            print()

            choice2 = int(input("Enter your choice: "))
            print()

            if choice2 == 1:
                print("Person Details:")
                print("Name:", person.name)
                print("Age:", person.age)
                print()

            elif choice2 == 2:
                print("Employee Details:")
                print("Name:", employee.em_name)
                print("Age:", employee.em_age)
                print("Employee ID:", employee.get_id())
                print("Salary:", employee.get_salary())
                print()

            elif choice2 == 3:
                print("Manager Details:")
                print("Name:", manager.em_name)
                print("Age:", manager.em_age)
                print("Employee ID:", manager.get_id())
                print("Salary:", manager.get_salary())
                print("Department:", manager.dep)
                print()

            else:
                print("Invalid choice.\n")

            print("--- Choose another operation ---\n")

        case 5:
            print("Exiting the system.")
            break
        
        case _:
            print("Invalid choice.\n")

print("Goodbye!")