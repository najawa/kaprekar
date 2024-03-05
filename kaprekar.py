import sys

if __name__ == '__main__':

	if len(sys.argv) >= 2:
		input_int = sys.argv[1]
	else:
		raise ValueError('4 Digit Number Expected as Input!')

	# Check if the number is a 4-digit number
	if (len(input_int) != 4):
		raise ValueError("Input is not a 4-digit number.")

	# Check if at least 2 digits are different
	if (len(set(input_int)) < 3):
		raise ValueError("At least two digits must be different.")


	if len(sys.argv) == 3:
		steps = sys.argv[2]
	else:
		steps = 10

	for i in range(steps, 0, -1):
		print('Number: ' + str(input_int))
		input_str = str(input_int);

		a = sorted(input_str, reverse=True)
		b = sorted(input_str, reverse=False)

		input_int = int(''.join(a)) - int(''.join(b))

		if (input_int == 6174):
			break;
	print('Number: ' + str(input_int))
	print('Ran for ' + str(steps - i + 1) + ' iterations')