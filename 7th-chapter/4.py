def eval_loop():
	print
	while True:
		string = raw_input('>>> ')
		if string == 'done':
			break
		result=eval(string)
		print result
	return result

print eval_loop()
