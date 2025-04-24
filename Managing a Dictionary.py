students = {  
    "Ron": {"grade": 85, "age": 20},
    "Jane": {"grade": 90, "age": 22},
    "Guy": {"grade": 78, "age": 19},
    "Gracie": {"grade": 92, "age": 21}
}

def print_students():
    print("\n Current student list:")
    for name, info in students.items():
        print(f"{name}: Grade = {info['grade']}, Age = {info['age']}")

print_students() 

decision = str(input("do you want to add a new student? (yes/no)")).lower()
if decision == "yes":
    new_student = str(input("Enter the name of the new student: "))
    new_grade = int(input("Enter the grade of the new student: "))
    new_age = int(input("Enter the age of the new student: "))  
    students[new_student] = {"grade": new_grade, "age": new_age}
    print("/n Student added successfully!")
    print_students() 
else:
    print("No new student added.")
    
name_to_update = input("\nEnter student name to update grade: ")
if name_to_update in students:
    updated_grade = int(input("Enter new grade: "))
    students[name_to_update]["grade"] = updated_grade
    print("Grade updated.")
else:
    print("Student not found.")
print_students()

name_to_delete = input("\nEnter student name to delete: ")
if name_to_delete in students:
    del students[name_to_delete]
    print("Student deleted.")
    print_students()
else:
    print("Student not found.")
    
class_avg = sum(student["grade"] for student in students.values()) / len(students)
print(f"\nClass average grade: {class_avg:.2f}")

best_student = max(students, key=lambda x: students[x]["grade"])
print(f"Best student: {best_student} with grade {students[best_student]['grade']}")
