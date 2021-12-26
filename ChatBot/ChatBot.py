print("Hello! My name is NesterenkoB19st_bot")
print("I was created in 2021")


name = input("Please, remind your name\n >")
print("Have a nice name,", name)

print("Let me guess your age\n")
print("Enter remainders of dividing your age by 3, 5, 7.")
remainder3 = int(input("remainder3:>"))
remainder5 = int(input("remainder5:>"))
remainder7 = int(input("remainder7:>"))
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("your age is,", age, ",its best time to start programing!")
