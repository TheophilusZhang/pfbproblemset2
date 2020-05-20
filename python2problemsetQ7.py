b = 1000
if b > 0:
	print(b, 'is positive')
	if b < 50:
		print(b, 'is smaller than 50')
		if b%2 == 0:
			print(b, 'is smaller than 50 and is an even number')
elif b > 50:
                if b%3 == 0:
                        print(b, 'is larger than 50 and divisible by 3')
elif b < 0:
        print(b, 'is negative')
else:
        print(b, 'is equal to 0')
