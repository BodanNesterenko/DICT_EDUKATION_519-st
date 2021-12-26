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


print("Now I will prove you that I can count to any number you want")
x = 0
y = int(input(">"))
while x <= y:
    print(x, "!")
    x = x + 1
print("Completed, have a nice day!")

print("Lets test your knowlege")
line_q1 = """
1.Kirill
2.Yaroslav
3.Vlad
4.Bogdan
"""
print("what is my name?", line_q1)
ansv = int(input("Input number of answer >"))
while True:
    if ansv == 4:
        print("Sucsess!!!")
        break
    else:
        print("Try again")
        ansv = int(input("Input number of answer >"))
print("Congratulation!!! Have a nice day")
