
_range = int(input())
for i in range(_range):
    n = i 
    temp = n 
    temp_size = n 
    length = 0 
    _sum = 0
    # is to find length of n
    while temp_size > 0:
        temp_size = int(temp_size/10)
        length+=1
    #  to find sum
    while n>0:
        rem = n%10 
        _sum += (rem**length) 
        n = int(n/10)

    # to compare
    if temp == _sum:
        print(f"{temp} is armstrong")
    # else:
    #     print(f"{temp} is not armstrong")
