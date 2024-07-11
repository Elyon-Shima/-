# Question 1: Hospital Patient Management System 
patients = []

def add_patient():
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    illness = input("Enter patient's illness: ")
    patient = {'name': name, 
               'age': age, 
               'illness': illness}
    patients.append(patient)
    print("Patient added successfully.\n")

def display_patients():
    if patients:
        print("List of Patients:")
        for patient in patients:
            print(f"Name: {patient['name']}, 
                  Age: {patient['age']}, 
                  Illness: {patient['illness']}")
    else:
        print("No patients in the system.\n")

def search_patient():
    name = input("Enter the name of the patient you want to search for: ")
    for patient in patients:
        if patient['name'] == name:
            print(f"Patient found - Name: {patient['name']}, 
                                    Age: {patient['age']}, 
                                    Illness: {patient['illness']}\n")
            return
    print("Patient not found.\n")

def remove_patient():
    name = input("Enter the name of the patient you want to remove: ")
    for patient in patients:
        if patient['name'] == name:
            patients.remove(patient)
            print(f"Patient '{name}' removed successfully.\n")
            return
    print("Patient not found.\n")

while True:
    print("Patient Management System")
    print("1. Add a new patient")
    print("2. Display all patients")
    print("3. Search for a patient by name")
    print("4. Remove a patient by name")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_patient()
    elif choice == '2':
        display_patients()
    elif choice == '3':
        search_patient()
    elif choice == '4':
        remove_patient()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.\n")
