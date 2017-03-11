#!/usr/bin/env python3

import operator

ops = {
	'+': operator.add,
	'-': operator.sub
}

def calculate(arg):
	stack = arg.split()
	command = stack.pop()
	try:
		arg2 = float(stack.pop())
		arg1 = float(stack.pop())
		stack.append(ops[command](arg1, arg2))
	except ValueError:
		stack.append(float(command))

	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()