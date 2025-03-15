# Nested for loop for multiplication table (1 to 5)
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()  # for a new line after each row
