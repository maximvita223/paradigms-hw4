def rec_sum(n):
    result = int(n)
    if n <= 1:
        return result 
    else:
        return result + rec_sum(n-1)

print(rec_sum(4))