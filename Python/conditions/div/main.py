n = int(input())

if n%3==0 and n%5==0:
    print(f"{n} is divisble by 3 & 5")
if n%5==0:
    print(f"{n} is divisble by 5")
if n%3 == 0:
    print(f"{n} is divisble by 3")
else:
    print(f"{n}It is not divisible by 3&5")

