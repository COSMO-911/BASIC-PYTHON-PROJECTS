import sys
while True:
    operator = input("Enter operator: ")
    result = 0 
    if operator in ["+" , "-" , "*" , "/"]:
        while True:
            try:
                num1 = int(input("enter number 1 : "))
                num2 = int(input("enter number 2 : "))
                break
            except ValueError:
                print("Input a number")
        if operator=="+":
            result= num1+num2
        elif operator=="-":
            result= num1-num2
        elif operator=="*":
            result= num1*num2
        elif operator=="/":
            divide_again = "y"
            trials = 0
            while divide_again == "y":
                
                if trials >=3:
                    break
                try:
                    result= num1 /num2
                    break
                except ZeroDivisionError:
                    print("cant divide by zero")
                    trials+=1
                    divide_again = input("press 'y' to divide again: ").lower()
                    num1 = int(input("enter number 1 : "))
                    num2 = int(input("enter number 2 : "))
                print("too many 0 division error")
                sys.exit()
        print(f"{num1} {operator} {num2} = {result}")
        again = input("press 'y' to reuse the calc. : ").lower()
        if again != "y":
            break
    else:
        print("choose from [+ - * /] ")

print("Bye bye")

