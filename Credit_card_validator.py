# Made with luhn alogrithm

'''
works with - (16 digit cards)
1)Visa
2)Mastercard
3)Discover
4)JCB (Japan Credit Bureau)
5)Diners Club International (Some US/Canada variations)
6)Rupay
'''

def main():
    isrunning = True
    while isrunning:
        Card_num = int(input("enter credit card number(16 digits) : "))
        numlst = [int(x) for x in str(Card_num)]

        if len(numlst) != 16:
            print("invalid Credit card number ")
            continue
        
        #Isolating last digit
        lastDigit = numlst.pop()

        #doubling every other number
        for i in range(0,15,2):
            numlst[i]*=2

        #adding digits bigger than 9
        for j in numlst:
            if j > 9:
                numlst[j] = j[0] + j[1]

        #sum every digit including  last isolated digit
        summ = sum(numlst) + lastDigit

        #Mod 10 test
        if summ%10 == 0:
            print("your credit card is Valid")
            isrunning = False
        else:
            print("invalid card")

main()
