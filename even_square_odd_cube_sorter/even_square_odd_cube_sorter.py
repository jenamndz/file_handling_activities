def process_integers():
    try:
        with open("integers.txt", "r") as input_file:
            with open("double.txt", "w") as double_file, open("triple.txt", "w") as triple_file: