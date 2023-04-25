# Franchesca Marie U. Donadillo
# BSCPE 1-5
# Program 1 - 20 Integers, Odd/ Even

# import pyfiglet
import pyfiglet

# import rich for color
from rich.theme import Theme
from rich.console import Console

# generate theme
theme_num = Theme({"congrats": "bold cyan", "checkout" : "bold italic green"})
console_num = Console(theme = theme_num)

# read a text file named numbers.txt
# create a text file named even.txt
# create a text file named odd.txt
with open("numbers.txt", "r") as file_numbers, open("even.txt", "w") as file_even, open("odd.txt", "w") as file_odd:
    
    # iterate through numbers.txt 
    i = 1   
    for line in file_numbers:
        num = int(line)
        if num % 2 == 0:
            file_even.write(f"Even #{i}: " + str(num) + "\n")
            i += 1

        elif num % 2 == 1:
            file_odd.write(f"Odd #{i}: " + str(num) + "\n")
            i += 0

congrats = pyfiglet.figlet_format("Congrats! ", font = "slant")
console_num.print(congrats, style = "congrats")
console_num.print("\n--Odd and even numbers are now in their respective text file. Check it out!--\n", style = "checkout")