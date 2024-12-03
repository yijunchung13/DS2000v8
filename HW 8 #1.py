def analyze_student_performance(students):
    import statistics

    averages = {student[0]: round(statistics.mean(student[1]), 2) for student in students}

    highest_avg = max(averages.values())
    top_students = [name for name, avg in averages.items() if avg == highest_avg]

    overall_average = round(statistics.mean([grade for _, grades in students for grade in grades]), 2)

    above_average_count = sum(avg > overall_average for avg in averages.values())

    subject_wise_highest = [max(grades) for grades in zip(*[student[1] for student in students])]

    return {
        "Average Grades": averages,
        "Top Student(s)": top_students,
        "Overall Average Grade": overall_average,
        "Students Above Overall Average": above_average_count,
        "Subject-Wise Highest Grades": subject_wise_highest
    }

students = [
    ("Alice", [85, 90, 78]),
    ("Bob", [92, 88, 84]),
    ("Charlie", [70, 75, 80])
]

results = analyze_student_performance(students)
for key, value in results.items():
    print(f"{key}: {value}")