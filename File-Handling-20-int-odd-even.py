# Franchesca Marie U. Donadillo
# BSCPE 1-5
# Program 1 - 20 Integers, Odd/ Even

# read a text file named numbers.txt
# create a text file named even.txt
# create a text file named odd.txt
with open("numbers.txt", "r") as file_numbers, open("even.txt", "w") as file_even, open("odd.txt", "w") as file_odd:
    # iterate through numbers.txt    
    for line in file_numbers:
        num = int(line)
        if num % 2 == 0:
            file_even.write(str(num) + "\n")
                        
        elif num % 2 == 1:
            file_odd.write(str(num) + "\n")
            