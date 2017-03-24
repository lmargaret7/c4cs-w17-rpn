#!/usr/bin/env python3

import operator

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
}


def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()
def calculate_3(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg3 = stack.pop()
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			int_result = operator_fn(arg1, arg2)
			fin_result = operator_fn(int_result, arg3)
			
			stack.append(fin_result)
	return stack.pop()

def main():
	while True:
		#result = calculate(input('rpn calc> '))
		result = calculate_3(input('rpn calc_3> '))
		print("Result:", result)

if __name__ == '__main__':
	main()
