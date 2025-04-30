bank = True
print("Hello and welcome to Shawn's Bank.")
op = input("Would you like to make a deposit. (yes/no): ")
if op.lower == "no":
    print("Okay, have a nice day!!!")
elif op.lower == "yes":
    print("Thank you for using this bank!")
    num = int(input("How much do you want to deposit?: "))
    op2 = input(f"Thank you for depositing {num}, would you like to see your deposit in Ph denominations? (yes/no): ")
    if op2.lower =="no":
            print(f"Thank you for using this bank, Your total deposit is {num}")
            
    elif op2.lower == "yes":
        thou = num // 1000
        thousukli = num % 1000

        fiveh = thousukli // 500
        fivesukli = thousukli % 500

        twoh = fivesukli // 200
        twosukli = fivesukli % 200

        oneh = twosukli // 100
        onesukli = twosukli % 100

        fifty = onesukli // 50
        fiftysukli = onesukli % 50

        twent = fiftysukli // 20
        twentsukli = fiftysukli % 20

        ten = twentsukli // 10
        tensukli = twentsukli % 10

        lima = tensukli // 5
        limasukli = tensukli % 5

        piso = limasukli // 1
        pisosukli = limasukli % 1

        print(f" {thou} - 1000")
        print(f" {fiveh} - 500")
        print(f" {twoh} -  200")
        print(f" {oneh} -  100")
        print(f" {fifty} -  50")
        print(f" {twent} -  20")
        print(f" {ten} -  10")
        print(f" {lima} -  5")
        print(f" {piso} -  1")
        print(f"There is your deposit of {num} in ph denominations, thank you for using this bank!!!")

    else:
        print("Mali yan nganiiiii")           
else:
    print("Invalid input, please try again") 
          
