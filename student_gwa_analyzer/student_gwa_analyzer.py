highest_gwa = -1.0
top_student = ""


try:
    with open("students_gwa.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) == 2:
                name = parts[0]
                gwa = float(parts[1])

                if gwa > highest_gwa:
                    highest_gwa = gwa
                    top_student = name