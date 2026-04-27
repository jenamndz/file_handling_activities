highest_gwa = -1.0
top_student = ""


try:
    with open("students_gwa.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")