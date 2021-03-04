while True:
	try:
		number = int(input("Whats your fav number hoss??\n"))
		print(18/number)
		break
	except ValueError:
		print("make sure and enter a number.")
	except ZeroDivisionError:
		print("Dont pick zero")
	except:
		break
	finally:
		print("loop complete")