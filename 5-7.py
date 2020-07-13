import random

lotto = random.randint(1,100)


num = int(input("복권 번호: "))
print("복권 번호 는 ", lotto, "입니다.")
if(lotto == num):
    print("축하합니다. 상금 100만원입니다.")
elif(lotto/10 == num/10 or lotto/10 == num%10 or lotto%10 == num/10 or lotto%10 == num%10):
    print("축하합니다. 상금 50만원입니다.")
else:
    print("탈락입니다")
