

def lengthOfN(n):
    length = 0
    while n > 0:
        length+=1
        n = int(n/10)
    return length 

def sumOfN(n, length):
    _sum = 0
    while n > 0:
        rem = n%10
        _sum += (rem ** length)
        n = int(n/10)
    return _sum 

def isArmstrong(n, _sum):
    if n == _sum:
        return True 
    else:
        return False 
# declaration

def armstrongInCertainRange(_range):
    for i in range(_range):
        n = i
        length = lengthOfN(n)
        _sum = sumOfN(n, length)

        if isArmstrong(n, _sum):
            print(f"{n} is armstrong")
        # else:
        #     print(f"{n} is not armstrong")









