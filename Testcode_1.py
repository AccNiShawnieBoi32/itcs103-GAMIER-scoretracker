bilis = True
odd = 0
even = []
while bilis == True:
    num = int(input("You have entered a loop, enter any number (To exit the loop just type the number '0'): "))
    if num == 0:
        print(f"The sum of all odd numbers are {odd}")
        print(even)
        break
    elif num % 2 != 0:
        odd += num
    elif num % 2 == 0:
        even.append(num)