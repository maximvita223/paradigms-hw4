def fibbonachi(n):
    if n <= 1:
        return n
    else:
        return fibbonachi(n-1) + fibbonachi(n-2)


number = 4
print(f"{number}-е число Фибоначчи = {fibbonachi(number)}")