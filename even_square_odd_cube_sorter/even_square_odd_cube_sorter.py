def process_integers():
    try:
        with open("integers.txt", "r") as input_file:
            with open("double.txt", "w") as double_file, open("triple.txt", "w") as triple_file:

                for line in input_file:
                    num_str = line.strip()
                    if num_str:
                        number = int(num_str)

                        if number % 2 == 0:
                            result = number ** 2
                            double_file.write(str(result) + "\n")
                        else:
                            result = number ** 3
                            triple_file.write(str(result) + "\n")

        print("Operation complete. Check 'double.txt' and 'triple.txt'.")

    # Error handling if the source file is missing
    except FileNotFoundError:
        print("Error: 'integers.txt' was not found.")


# Call the method
process_integers()