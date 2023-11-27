def evenNums(num):
    print(num)
    if num % 2 != 0:
        print("Please enter an even number.")
    elif num == 2:
        return num
    else:
        return evenNums(num - 2)
    
evenNums(9)