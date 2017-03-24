#!/usr/bin/env python3

import operator
from colorama import *

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
		user_in = input('rpn calc> ')
		
		result = calculate(user_in)
		for operand in user_in.split():
		    try:
			    if float(operand) < 0:
				    print Back.RED + operand,
			    else:
				    print operand,
		    except:
		        print Back.GREEN + operand,

		print(Style.RESET_ALL)
		
		#result = calculate_3(input('rpn calc_3> '))
		print("Result:", result)

if __name__ == '__main__':
	main()
