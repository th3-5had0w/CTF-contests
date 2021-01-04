#!/usr/bin/env python3.6

import random
import sys


def get_value(n):
    value = 0
    for i in range(len(n)):
        value = 10*value + (ord(n[i]) - 0x30)
    return value


def menu():
    print("1. Test your luck")
    print("2. Buy flag")
    print("3. Exit")


def luck(money):
    print("How much do you wanna bet?")
    print("> ", end="")
    bet = input().strip().replace('+', '').replace('-', '')
    print(bet)
    
    try:
        int(bet)
        bet.encode("ascii")
    except:
        print("Invalid number")
        return money
    
    if int(bet) > money:
        print("Can't bet more than what you have")
        return money
    else:
        if random.randint(1, 10) == 1:
            print("You win {}$".format(bet))
            return money + get_value(bet)
        else:
            print("You lose {}$".format(10))
            return money - 10


def flag(money):
    if money > 696969696969:
        flag = open("./flag.txt", "r").read()
        print(flag)
        sys.exit()
    else:
        print("Not enough money")


if __name__ == "__main__":
    money = 69
    while True:
        menu()
        print("Money: {}$".format(money))

        try:
            print("> ", end="")
            choice = int(input())
        except:
            choice = 0

        if choice == 1:
            money = luck(money)
        elif choice == 2:
            flag(money)
        elif choice == 3:
            sys.exit()
        else:
            print("Invalid choice")
