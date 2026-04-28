def write_to_mylife():
    with open("mylife.txt", "w") as myFile:

        while True:
            line = input("Enter line: ")

            myFile.write(line + "\n")

            choice = input("Are there more lines y/n? ").lower()

            if choice == 'n':
                break

    print("Data saved to mylife.txt successfully.")

write_to_mylife()