from random import randint

firVal = randint(1,10)
secVal = randint(1,10)
action = ['+','-','*','/']
if not secVal == 0:
	raction = randint(0,3)
else:
	raction = randint(0,2)

if raction == 0:
	result = firVal + secVal
elif raction == 1:
	result = firVal - secVal 
elif raction == 2:
	result = firVal * secVal
elif raction == 3:
	result = firVal / secVal

uresult = ''
while not uresult == result:
	print(firVal, action[raction], secVal, '= ', end='')
	uresult = input()

	if uresult == 'q':
		print('correct answer:', result)
		break

	elif int(result) == int(uresult):
		print("success")
		break
	else:
		print('wrong input, type q to exit')

