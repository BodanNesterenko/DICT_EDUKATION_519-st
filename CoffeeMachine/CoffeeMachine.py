money = 550
coffee = 120
water = 400
milk = 540
cups = 9


class ResourceError(Exception):
    pass


def print_parametrs():
    print("Coffee machine has:")
    print(money, "UAH")
    print(coffee, "grams of coffee")
    print(water, "ml of water")
    print(milk, "ml of milk")
    print(cups, "Cups")


def select_action():
    return input("CHOOSE ACTION\n-buy\n-fill\n-take\n-remaining\n-exit\n>")


def select_drink() -> int:
    back = input("What are you want to buy\n1-espresso\n2-latte\n3-cappuccino\nback - to main menu\n>")
    if back == "back":
        return main()
    return int(back)


def is_enough(need_water=0, need_milk=0, need_coffee=0):
    if water < need_water:
        print("Sorry, not enough water!\n")
        raise ResourceError
    if milk < need_milk:
        print("Sorry, not enough milk!\n")
        raise ResourceError
    if coffee < need_coffee:
        print("Sorry, not enough beans!\n")
        raise ResourceError
    if cups < 1:
        print("Sorry, not enough cups\n")
        raise ResourceError
    print("I have enough resources, making you a coffee!\n")


def buy_drinks():
    global money, coffee, milk, water, cups
    drink = select_drink()

    try:
        if drink == 0:
            pass
        if drink == 1:
            is_enough(need_water=250, need_coffee=16)
            money += 4
            water -= 250
            coffee -= 16
            cups -= 1
        elif drink == 2:
            is_enough(need_water=350, need_coffee=20, need_milk=75)

            money += 7
            water -= 350
            milk -= 75
            coffee -= 20
            cups -= 1
        elif drink == 3:
            is_enough(need_water=350, need_milk=100, need_coffee=12)
            money += 6
            water -= 200
            milk -= 100
            cups -= 1
        else:
            raise ValueError
    except ResourceError:
        pass


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

    while True:
        action = select_action()

        if action == "buy":
            buy_drinks()
        elif action == "fill":
            fill_machine()
        elif action == "take":
            take_money()
        elif action == "exit":
            exit()
        elif action == "remaining":
            print_parametrs()


main()
