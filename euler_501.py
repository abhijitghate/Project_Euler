
answer_dict = {}

def num_divisor(x):
	divisors = []
	for i in range(1,x+1):
		if x%i == 0:
			divisors.append(i)
	answer_dict.update({x:divisors})


count = 0 
for i in xrange(1,10**12):
	num_divisor(i)

for i in answer_dict:
	if len(answer_dict[i]) == 8:
		count = count + 1
print count

#This is just a tryout

