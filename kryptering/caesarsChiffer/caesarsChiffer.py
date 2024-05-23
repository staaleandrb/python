import os

def read_file(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read(5)  # Read the first 5 characters
            print(content)  # Print the first 5 characters
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Print the current working directory to verify
print("Current working directory:", os.getcwd())

# Example usage:
read_file("c:/xampp/htdocs/repos/python/kryptering/caesarsChiffer/kryptert_1.txt")
