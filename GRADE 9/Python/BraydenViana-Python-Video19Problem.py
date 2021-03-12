places = ("usa", "mexico", "portugal", "china", "canada")
guess = str(input("Please input a country: "))

if guess in places:
        print("Yes")

if guess not in places:
        print("Not in our database")

