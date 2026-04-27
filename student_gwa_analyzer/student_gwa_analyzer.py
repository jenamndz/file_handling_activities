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

    if top_student:
        print(f"The student with the highest GWA is {top_student} with a GWA of {highest_gwa}")
    else:
        print("The file was empty.")

except FileNotFoundError:
    print("Error: 'students.txt' not found. Please create the file first.")
except ValueError:
    print("Error: Ensure the GWA is a valid number and formatted correctly.")