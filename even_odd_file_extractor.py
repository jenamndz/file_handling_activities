try:
    with open("numbers.txt", "r") as input_file:
        with open("even.txt", "w") as even_file, open("odd.txt", "w") as odd_file: