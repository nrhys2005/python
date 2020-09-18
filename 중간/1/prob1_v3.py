
def digit_sum(n):
    sum = 0
    while n > 0 :
        digit = n%10
        sum += digit 
        n = int(n / 10)
    return sum
        
def digitList(n):
    list = []
    while n > 0 :
        digit = n%10
        list.append(digit)
        n = int(n / 10)
    return list
    
print( "각 자리의 수들의 합 : ", digit_sum(1234) ) 
print( "추출된 리스트 : ", digitList(1234) ) 
