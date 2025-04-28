students = [
    {"name": "Alice", "grades": [90, 85, 88]},
    {"name": "Bob", "grades": [45, 50, 55]},
    {"name": "Charlie", "grades": [95, 92, 94]},
    {"name": "David", "grades": [30, 40, 45]},
    {"name": "Eve", "grades": [88, 90, 85]},
    {"name": "Frank", "grades": []} ]


def calculate_average(student):
    if student["grades"]:
        avg = round(sum(student["grades"]) / len(student["grades"]), 2)
    else:
        avg = None
    return {"name": student["name"], "average": avg}

averages = list(map(calculate_average, students))

print("\n🎯 Students and their averages:")
for student in averages:
    if student["average"] is not None:
        print(f"{student['name']}: {student['average']:.2f}")
    else:
        print(f"{student['name']}: No grades available")


passed_students = list(filter(lambda s: s["average"] is not None and s["average"] >= 50, averages))

print("\n✅ Students who passed:")
for student in passed_students:
    print(f"{student['name']}: {student['average']:.2f}")


sorted_students = sorted(
    filter(lambda s: s["average"] is not None, averages),
    key=lambda s: s["average"],
    reverse=True
)

print("\n🏆 Students sorted by average grade (highest first):")
for student in sorted_students:
    print(f"{student['name']}: {student['average']:.2f}")


updated_students = list(map(
    lambda s: {
        "name": s["name"],
        "grades": [min(grade + 5, 100) for grade in s["grades"]]
    },
    students
))

print("\n🔧 Updated grades (after adding 5 points):")
for student in updated_students:
    print(f"{student['name']}: {student['grades']}")


print("\n⚠️ Checking for students with no grades:")
for student in students:
    if not student["grades"]:
        print(f"{student['name']} has no grades available.")


summary = [(student["name"], student["average"]) for student in averages if student["average"] is not None]


highest_grade = max((grade for student in students for grade in student["grades"]), default=None)


top_students = list(filter(lambda s: highest_grade in s["grades"], students))

print("\n📄 Summary Report:")
if highest_grade is not None:
    print(f"Highest grade in the class: {highest_grade}")
    print("Student(s) with the highest grade:")
    for student in top_students:
        print(f"- {student['name']}")
else:
    print("No grades available to calculate the highest grade.")

    