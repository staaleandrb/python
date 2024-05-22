def read_file():
    with open("kryptert_1.txt", "r") as f:
        content = f.read(5)  # Read the first 5 characters
        print(content)  # Print the first 5 characters

read_file()