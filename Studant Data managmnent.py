students = { 
    "Yael": {
        "age": 25,
        "subjects": ["math", "science", "history"],
        "grades": {"math": 90, "science": 85, "history": 88}
},
    "Jane": {
        "age": 22,
        "subjects": ["math", "science", "english"],
        "grades": {"math": 92, "science": 89, "english": 91} 
},
    "Guy": {
        "age": 20,
        "subjects": ["math", "art", "history"],
        "grades": {"math": 78, "art": 82, "history": 80}
},
    "Gracie": {
        "age": 21,
        "subjects": ["math", "science", "art"],
        "grades": {"math": 95, "science": 90, "art": 93}
}
}
print("\ncurrent student list:")
for name, info in students.items():
    print(f"{name}: Age = {info['age']}, Subjects = {', '.join(info['subjects'])}, Grades = {info['grades']}")
    
print("\ndo you want to add a new student? (yes/no)")
decision = str(input()).lower() 
if decision == "yes":
    new_student = str(input("enter the name of the new student: "))
    new_age = int(input("enter the age of the new student: "))
    new_subjects = str(input("enter the subjects of the new student (comma separated): ")).split(",")
    new_grades = {}
    for subject in new_subjects:
        grade = int(input(f"enter the grade for {subject.strip()}: "))
        new_grades[subject.strip()] = grade
    students[new_student] = {"age": new_age, "subjects": [subject.strip() for subject in new_subjects], "grades": new_grades}
    print("\nstudent added successfully!")
for name, info in students.items():
    print(f"{name}: Age = {info['age']}, Subjects = {', '.join(info['subjects'])}, Grades = {info['grades']}")
if decision == "no":
    print("\nOK, No student added.")

print("\ndo you want to update a student's grades? (yes/no)")
decision = str(input()).lower() 
if decision == "yes":
    name_to_update = str(input("enter student name to update: "))
    if name_to_update in students:
        subject_to_update = str(input("enter the subject to update: "))
        if subject_to_update in students[name_to_update]["grades"]:
            new_grade = int(input(f"enter the new grade for {subject_to_update}: "))
            students[name_to_update]["grades"][subject_to_update] = new_grade
            print("\ngrade updated successfully!")
        else:
            print("\nsubject not found.")
    else:
        print("\nstudent not found.")
for name, info in students.items(): 
    print(f"{name}: Age = {info['age']}, Subjects = {', '.join(info['subjects'])}, Grades = {info['grades']}")
if decision == "no":
    print("\nOK, No grades updated.")
    
print("\ndo you want to delete a subject? (yes/no)")
decision = str(input()).lower()        
if decision == "yes":
    name_to_delete = str(input("Enter the name of the student to delete: "))
    if name_to_delete in students:
        subject_to_delete = str(input("Enter the subject to delete: "))
        if subject_to_delete in students[name_to_delete]["subjects"]:
            del students[name_to_delete]["grades"][subject_to_delete]
            students[name_to_delete]["subjects"].remove(subject_to_delete)
            print("\nsubject deleted successfully!")
        else:
            print("\nsubject not found.")
    else:
        print("\nstudent not found.")
        for name, info in students.items():
            print(f"{name}: Age = {info['age']}, Subjects = {', '.join(info['subjects'])}, Grades = {info['grades']}")
if decision == "no":
    print("\nOK, No subject deleted.")  
    
print("\ndo you wnat to calculate student\'s average grade? (yes/no)")
decision = str(input()).lower()
if decision == "yes":
    name_to_calculate = str(input("enter the name of the student to calculate average grade: "))
    if name_to_calculate in students:
        grades = students[name_to_calculate]["grades"].values()
        average_grade = sum(grades) / len(grades)
        print(f"\naverage grade for {name_to_calculate}: {average_grade:.2f}")
    else:
        print("\nStudent not found.")
for name, info in students.items():
    print(f"{name}: Age = {info['age']}, Subjects = {', '.join(info['subjects'])}, Grades = {info['grades']}")
if decision == "no":
    print("\nOK, No average grade calculated.")
    
print("\ndo you want to find the best student? (yes/no)")
decition = str(input()).lower()
if decision == "yes":
    best_student = max(students, key=lambda x: sum(students[x]["grades"].values()) / len(students[x]["grades"]))
    best_student_avg = sum(students[best_student]["grades"].values()) / len(students[best_student]["grades"])
    print(f"\nbest student: {best_student}, average grade: {best_student_avg:.2f}")
if decition == "no":
    print("\nOK, may be next time.")
    
student_tuples = []
for name, info in students.items():
    age = info["age"]
    num_subjects = len(info["subjects"])
    student_tuples.append((name, age, num_subjects))
    sorted_students = sorted(student_tuples, key=lambda x: x[1])
    
for student in sorted_students:
    print(f"\nName: {student[0]}, Age: {student[1]}, Number of Subjects: {student[2]}")