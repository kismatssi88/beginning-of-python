import pandas as pd

students = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105],
    "name": ["Aarav", "Sita", "Ram", "Priya", "Kiran"],
    "age": [16, 15, 16, 17, 15],
    "class": [10, 9, 10, 11, 9]
})

print(students)
marks = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105],
    "math": [88, 75, 92, 80, 69],
    "science": [91, 70, 89, 85, 74],
    "english": [85, 82, 78, 90, 76]
})

print(marks)
schools = pd.DataFrame({
    "school_id": [1, 2, 3],
    "school_name": [
        "Everest School",
        "Himalaya Academy",
        "Sunrise School"
    ],
    "city": ["Kathmandu", "Pokhara", "Butwal"]
})

print(schools)
student_school = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105],
    "school_id": [1, 2, 1, 3, 2]
})

print(student_school)
result = pd.merge(student_school, students, on="student_id")
result = pd.merge(result, schools, on="school_id")

print(result)