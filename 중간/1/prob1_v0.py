n = 1234
sum = 0
while n > 0 :
    digit = n%10
    print(digit)
    sum += digit 
    n = int(n / 10)
    
print( "각 자리의 수들의 합 :", sum ) 
