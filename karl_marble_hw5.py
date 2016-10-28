#!/usr/bin/env python3
import sys

def valid():
    """
    Takes a 4 digit input and checks it against a valid code.
    Args:
        None
    Returns:
        None
    """
    #0) Loop three times through the following steps)
    #1) Take the Pin Input
    #2) Check the length
    #2) Check the type
    #3) Check against the code
    for i in range(3):
        pin = input("Enter your PIN:")
        strLength = len(pin)
        if strLength > 4:
            print("Invalid PIN length. Correct format is <9876>")
        try:
            pinVal = int(pin)
        except ValueError:
            print("Invalid Pin Character. Correct format is <9876>")
        if pin == "1234":
            print("Your PIN is correct.")
            return
    print("Your bank card is blocked.")
    exit (1)


def main():
    """
    Test Function
    """
    valid()

if __name__ == '__main__':
    #call main
    main() 

    exit(0)
