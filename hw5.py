from random import randint

l1 = list()


for i in range(0,10):
	l1.append(randint(1,100))	

print(l1)

l2 = list()

for i in range(0,10):
	if not l1[i] % 7 and l1[i] % 5:
		l2.append(l1[i])
print(l2)