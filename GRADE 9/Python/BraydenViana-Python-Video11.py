numberstaken = [2, 5, 12, 13, 18]

print("Here are the numbers that are still avaliable")

for n in range(1, 20):
	if n in numberstaken:
		continue
	print(n)