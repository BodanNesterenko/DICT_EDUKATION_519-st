water = 200
milk = 50
coffee = 15

user_input = int(input("How many cup of coffee you need:" "\n>"))

needed_milk = 200*user_input
needed_water = 50*user_input
needed_coffe = 15*user_input
print("For", user_input, "Cup of coffee tou will need:")
print("Water=", needed_water, "ml." "\nMilk=", needed_milk, "ml." "\nCoffee=", needed_coffe, "g.")
