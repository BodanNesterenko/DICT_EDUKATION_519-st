money = 550
coffee = 120
water = 400
milk = 540
cups = 9


def print_parametrs():
    print("Coffee machine has:")
    print(money, "UAH")
    print(coffee, "grams of coffee")
    print(water, "ml of water")
    print(milk, "ml of milk")
    print(cups, "Cups")


def select_action():
    return input("CHOOSE ACTION\n-buy\n-fill\n-take\n>")


def select_drink():
    return int(input("What are you want to buy\n1-espresso\n2-latte\n3-cappuccino\n>"))


def buy_drinks():
    global money, coffee, milk, water, cups
    drink = select_drink()

    if drink == 1:
        assert coffee >= 250
        assert water >= 16
        money += 4
        coffee -= 16
        water -= 250
    elif drink == 2:
        assert coffee >= 20
        assert water >= 350
        assert milk >= 75
        money += 7
        water -= 350
        milk -= 75
    elif drink == 3:
        assert coffee >= 12
        assert water >= 200
        assert milk >= 100
        money += 6
        water -= 200
        milk -= 100

    cups -= 1


def fill_machine():
    global water, coffee, milk, cups
    water += int(input("Write how many ml of water do you want to add\n>"))
    milk += int(input("Write how many ml of milk do you want to add\n>"))
    coffee += int(input("Write how many grams of coffee do you want to add\n>"))
    cups += int(input("Write how many cups do you want to add\n>"))


def take_money():
    global money
    print("I give you", money, "money")
    money = 0


def main():
    print_parametrs()

    action = select_action()
    if action == "buy":
        buy_drinks()
    elif action == "fill":
        fill_machine()
    elif action == "take":
        take_money()

    print(print_parametrs())


main()
