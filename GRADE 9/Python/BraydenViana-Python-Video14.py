def get_gender(sex='unknown'):
	if sex == 'm':
		sex = 'male'
	elif sex == 'f':
		sex = 'female'
	print(sex)

get_gender('m')
get_gender('f')
get_gender()
