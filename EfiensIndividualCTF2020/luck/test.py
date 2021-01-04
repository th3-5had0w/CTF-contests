def luck(money):
    print("How much do you wanna bet?")
    print("> ", end="")
    bet = input().strip().replace('+', '').replace('-', '')
    try:
        int(bet)
        bet.encode("ascii")
    except:
        print("Invalid number")
        return money
    if int(bet) > money:
        print("Can't bet more than what you have")
        return money
    print("HACKED!")


while 1:
    luck(69)
