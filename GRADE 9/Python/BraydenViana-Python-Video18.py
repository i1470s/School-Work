def health_calculator(age, apples_ate, cigs_smoked):
	awnser = (100 * age) + (apples_ate * 3.5) - (cigs_smoked * 2)
	print(awnser)

buckys_data = [27, 70, 0]

health_calculator(buckys_data[0], buckys_data[1], buckys_data[2])
health_calculator(*buckys_data)