# Franchesca Marie U. Donadillo
# BSCPE 1-5
# Program 1 - 20 Integers, Odd/ Even

# create a text file named numbers.txt
with open("numbers.txt", "a") as file_numbers:
    
    int_num = input("Please enter 20 integer numbers (use comma): ")

    file_numbers.write(str(int_num.split(",")))
# create a text file named even.txt
# create a text file named odd.txt