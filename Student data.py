import pickle
filename = "student_records.dat"
def add_record():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    math_marks = float(input("Enter Math Marks: "))
    cs_marks = float(input("Enter Computer Science Marks: "))
    record = [roll, name, math_marks, cs_marks]
    with open(filename, "ab") as f:
        pickle.dump(record, f)
        print("Record added successfully")

def display_records():
    try:
        with open(filename, "rb") as f:
            print("\n\t Student Records")
            while True:
                try:
                    rec = pickle.load(f)
                    print(f"Roll: {rec[0]}, Name: {rec[1]}, Math:{rec[2]}, CS: {rec[3]}")
                except EOFError:
                    break
    except FileNotFoundError:
        print("No records found")

def update_record():
    found = False
    records = []
    roll = int(input("Enter Roll No to update: "))
    try:
        with open(filename, "rb") as f:
            while True:
                try:
                    rec = pickle.load(f)
                    if rec[0] == roll:
                        print("Current record:", rec)
                        rec[2] = float(input("Enter new Math Marks: "))
                        rec[3] = float(input("Enter new ComputerScience Marks: "))
                        found = True
                    records.append(rec)
                except EOFError:
                    break
    except FileNotFoundError:
        print("No records found to update")
        return
    with open(filename, "wb") as f:
        for rec in records:
            pickle.dump(rec, f)
    if found:
        print("Record updated successfully")
    else:
        print("Record not found")

def delete_record():
    found = False
    records = []
    roll = int(input("Enter Roll No to delete: "))
    try:
        with open(filename, "rb") as f:
            while True:
                try:
                    rec = pickle.load(f)
                    if rec[0] != roll:
                        records.append(rec)
                    else:
                        found = True
                except EOFError:
                    break
    except FileNotFoundError:
        print("No records found to delete")
        return
    with open(filename, "wb") as f:
        for rec in records:
            pickle.dump(rec, f)
    if found:
        print("Record deleted successfully")
    else:
        print("Record not found")
while True:
 print("\tStudent Record Management")
 print("1. Add Record")
 print("2. Display Records")
 print("3. Update Record")
 print("4. Delete Record")
 print("5. Exit")
 choice = input("Enter choice: ")
 if choice == "1":
    add_record()
 elif choice == "2":
    display_records()
 elif choice == "3":
    update_record()
 elif choice == "4":
    delete_record()
 elif choice == "5":
    break
 else:
    print("Invalid choice")
