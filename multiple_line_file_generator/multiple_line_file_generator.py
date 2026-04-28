def write_to_mylife():
    with open("mylife.txt", "w") as myFile:

        while True:
            line = input("Enter line: ")

            myFile.write(line + "\n")

            choice = input("Are there more lines y/n? ").lower()

            if choice == 'n':
                break