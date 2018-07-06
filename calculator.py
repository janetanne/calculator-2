"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""
import sys

from arithmetic import *

while True:
	user_input = input()
	user_input.strip()
	user_input = user_input.split(" ")


	if user_input[0] == "q":
		print("You have exited the calculator.")
		sys.exit()

	else:
		num1 = float(user_input[1]) 

		if user_input[0] == "square":
			print(square(num1))

		elif user_input[0] == "cube":
			print(cube(num1))
			
		else:
			num2 = float(user_input[2])

			if user_input[0] == "+":
				print(add(num1, num2))
 
			elif user_input[0] == "-":
				print(subtract(num1, num2))

			elif user_input[0] == "*":
				print(multiply(num1, num2))

			elif user_input[0] == "/":
				print(divide(num1, num2))

			elif user_input[0] == "pow":
				print(power(num1, num2))

			elif user_input[0] == "mod":
				print(mod(num1, num2))

