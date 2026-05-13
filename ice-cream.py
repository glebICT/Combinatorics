flavors = ['chocolate', 'vanilla', 'strawberry']
toppings = ['sprinkles', 'nuts']
sauces = ['chocolate syrup', 'caramel']

for flavor in flavors:
	for topping in toppings:
		for sauce in sauces:
			print(f"{flavor} ice cream with {topping} and {sauce}")
