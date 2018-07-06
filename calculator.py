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

	elif user_input[0] == "+":
		print(add(int(user_input[1]), int(user_input[2])))


