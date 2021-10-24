while True:
    f1=int(input("Please enter the first number>>>"))
    sel = input("Please select an operator(+ - * /)\nplease write it down>>>")
    f2= int(input("enter the second number>>>"))

    print("\n\n\n<result>")
    if sel == "+":
        print(" " + str(f1 + f2))
    elif sel == "-":
        print(" " + str(f1 - f2))
    elif sel == "*":
        print(" " + str(f1 * f2))
    elif sel == "/":
        print(" " + str(f1 / f2))
    else:
        print("((Something went wrong... please re-enter))")
    input("Please press Enter to continue...")