water = 400
money = 550
milk = 540
coffee = 120 
cups = 9

def menu():
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(coffee, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")

def abstracction(wt, mk, cf):
    global water
    global milk
    global coffee
    global cups
    flag = True
    if water - wt < 0:
        print("Sorry, not enough water!")
        cups += 1
        flag = False
    elif milk - mk < 0:
        print("Sorry, not enough milk!")
        cups += 1
        flag = False
    elif coffee - cf < 0:
        print("Sorry, not enough coffee beans!")
        cups += 1
        flag = False
    return flag
def buy():
    global water
    global money
    global milk
    global coffee
    global cups
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino,  back - to main menu:")
    x = input("> ")
    if cups > 0:
        if x != "back":
            cups = cups - 1
        if x == "1":
            if abstracction(250, 0, 16):            
                water = water - 250
                coffee = coffee - 16
                money = money + 4
                print("I have enough resources, making you a coffee!")
        elif x == "2":
            if abstracction(350, 75, 20):   
                water = water - 350
                coffee = coffee - 20
                milk = milk - 75
                money = money + 7
                print("I have enough resources, making you a coffee!")
        elif x == "3":
            if abstracction(200, 100, 12):   
                water = water - 200
                coffee = coffee - 12
                milk = milk - 100
                money = money + 6
                print("I have enough resources, making you a coffee!")
    else:
        print("Sorry, not enough disposable cups!")
    print()
def fill():
    global water
    global money
    global milk
    global coffee
    global cups
    print("Write how many ml of water do you want to add:")
    x = int(input("> "))
    water = water + x
    print("Write how many ml of milk do you want to add:")
    x = int(input("> "))
    milk = milk + x
    print("Write how many grams of coffee beans do you want to add:")
    x = int(input("> "))
    coffee = coffee + x
    print("Write how many disposable cups of coffee do you want to add:")
    x = int(input("> "))
    cups = cups + x
    print()
def take():
    global money
    print("I gave you $" + str(money))
    money = 0
    print()


while True:
    print("Write action (buy, fill, take, remaining, exit):")
    orden = input("> ")
    if orden == "exit":
        break
    elif orden == "remaining":
        print()
        menu()
        print()
    elif orden == "buy":
        buy()
    elif orden == "fill":
        fill()
    elif orden == "take":
        take()
