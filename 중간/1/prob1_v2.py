
def digit_sum(n):
    sum = 0
    while n > 0 :
        digit = n%10
        sum += digit 
        n = int(n / 10)
    return sum
        

    
print( "각 자리의 수들의 합 : ", digit_sum(1234) ) 
