val = int(input("Enter the number of text files you want to create: "))

for i in range(1, val + 1):
    with open(f"file{i}.txt", "w") as f:
        pass  # Creates an empty text file

print(f"{val} text files have been created.")

    