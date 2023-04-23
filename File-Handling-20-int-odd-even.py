# Franchesca Marie U. Donadillo
# BSCPE 1-5
# Program 1 - 20 Integers, Odd/ Even

# create a text file named numbers.txt
with open("numbers.txt", "w") as file_numbers:
    
    int_num = input("Please enter 20 integer numbers (use comma): ")

    file_numbers.write(str(int_num.split(",")))

# create a text file named even.txt
with open("numbers.txt", "r") as file_numbers, open("even.txt", "w") as file_even:
    for line in file_numbers:
        line = (chr(48))
        file_even.write(line + 2)
# create a text file named odd.txt