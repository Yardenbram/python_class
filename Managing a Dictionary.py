students = {  
    "Ron": {"grade": 85, "age": 20},
    "Jane": {"grade": 90, "age": 22},
    "Guy": {"grade": 78, "age": 19},
    "Gracie": {"grade": 92, "age": 21}
}

def print_students():
    print("\n📚 Current student list:")
    for name, info in students.items():
        print(f"{name}: Grade = {info['grade']}, Age = {info['age']}")

print_students()