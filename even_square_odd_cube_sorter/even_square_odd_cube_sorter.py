def process_integers():
    try:
        with open("integers.txt", "r") as input_file:
            with open("double.txt", "w") as double_file, open("triple.txt", "w") as triple_file:

                for line in input_file:
                    num_str = line.strip()
                    if num_str:
                        number = int(num_str)