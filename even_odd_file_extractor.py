try:
    with open("numbers.txt", "r") as input_file:
        with open("even.txt", "w") as even_file, open("odd.txt", "w") as odd_file:

    for line in input_file:
        num_str = line.strip()

        if num_str:
            number = int(num_str)

            if number % 2 == 0:
                even_file.write(str(number) + "\n")
            else:
                odd_file.write(str(number) + "\n")

    print("Success! Check even.txt and odd.txt in your folder.")

except FileNotFoundError:
    print("Error: Ensure 'numbers.txt' is in the same folder as your script.")