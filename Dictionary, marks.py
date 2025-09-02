import random as r
students = {}
def add_record():
    student = {}
    sid = int(input("Enter student ID: "))
    if sid in students:
        print("ID Already Exists.")
        return
    student['name'] = input("Enter Student Name: ")
    student['math_mark'] = r.randint(35,100)
    student['phy_mark'] = r.randint(35, 100)
    student['che_mark'] = r.randint(35, 100)
    students[sid] = student
    print("Record Added Successfully.")
def delete_record():
    sid = int(input("Enter Student ID to Delete: "))
    if sid in students:
        del students[sid]
        print("Record deleted successfully")
    else:
        print("ID not Found.")
def print_records_descending():
    if not students:
        print("No Records to Display.")
        return
    sorted_students = sorted(students.items(), key=lambda item:(item[1]['math_mark']+
                      item[1]['phy_mark']+ item[1]['che_mark'])/3, reverse=True)
    print("\nID\tName\tMath\tPhysics\tChemistry\tAverage")
    for sid, data in sorted_students:
        avg = (data['math_mark']+ data['phy_mark']+ data['che_mark'])/3

print(f"{sid}\t{data['name']}\t{data['math_mark']}\t{data['phy_mark']}\t{data['che_mark']}\t\t{avg:.2f}")
ch = 'yes'
while ch.lower() in ['yes', 'y']:
    print("\nMenu:\n1. Add New Records\n2. Delete Record\n3. Print Records(Descending order of average)")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_record()
    elif choice == "2":
        delete_record()
    elif choice == "3":
        print_records_descending()
    else:
        print("Invalid Choice.")
    ch = input("Do you want to continue? (yes/y): ")
