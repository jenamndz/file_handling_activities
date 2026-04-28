def write_to_mylife():
    with open("mylife.txt", "w") as myFile:

        while True:
            line = input("Enter line: ")

            myFile.write(line + "\n")