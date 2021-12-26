class ResourceError(Exception):
    pass


class CoffeeMachine(object):
    """CoffeeMachine"""
    running = False

    def __init__(self, water=400, money=550, coffee=120, milk=540, cups=9):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

        if not CoffeeMachine.running:
            self.main()

    def print_parametrs(self):
        print("Coffee machine has:")
        print(self.money, "UAH")
        print(self.coffee, "grams of coffee")
        print(self.water, "ml of water")
        print(self.milk, "ml of self.milk")
        print(self.cups, "Cups")

    def select_action(self) -> str:
        return input("CHOOSE ACTION\n-buy\n-fill\n-take\n-remaining\n-exit\n>")

    def select_drink(self) -> int:
        back = input("What are you want to buy\n1-espresso\n2-latte\n3-cappuccino\nback - to main menu\n>")
        if back == "back":
            return self.main()
        return int(back)

    def is_enough(self, need_water=0, need_milk=0, need_coffee=0):

        if self.water < need_water:
            print("Sorry, not enough water!\n")
            raise ResourceError
        if self.milk < need_milk:
            print("Sorry, not enough self.self.milk!\n")
            raise ResourceError
        if self.coffee < need_coffee:
            print("Sorry, not enough beans!\n")
            raise ResourceError
        if self.cups < 1:
            print("Sorry, not enough cups\n")
            raise ResourceError
        print("I have enough resources, making you a coffee!\n")

    def buy_drinks(self):
        drink = self.select_drink()

        try:
            if drink == 0:
                pass
            if drink == 1:
                self.is_enough(need_coffee=16, need_water=250)

                self.money += 4
                self.water -= 250
                self.coffee -= 16
                self.cups -= 1
            elif drink == 2:
                self.is_enough(need_water=350, need_coffee=20, need_milk=75)

                self.money += 7
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.cups -= 1
            elif drink == 3:
                self.is_enough(need_water=350, need_milk=100, need_coffee=12)

                self.money += 6
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.cups -= 1
        except ValueError:
            self.main()

    def fill_machine(self):
        while input == "":
            self.water += int(input("Write how many ml of water do you want to add\n>"))
            self.milk += int(input("Write how many ml of self.milk do you want to add\n>"))
            self.coffee += int(input("Write how many grams of coffee do you want to add\n>"))
            self.cups += int(input("Write how many cups do you want to add\n>"))

    def take_money(self):
        print("I give you", self.money, "money")
        self.money -= self.money

    def main(self):
        self.running = True
        self.print_parametrs()

        while True:
            action = self.select_action()

            if action == "buy":
                self.buy_drinks()
            elif action == "fill":
                self.fill_machine()
            elif action == "take":
                self.take_money()
            elif action == "exit":
                exit()
            elif action == "remaining":
                self.print_parametrs()


CoffeeMachine(water=400, money=550, coffee=120, milk=540, cups=9)
