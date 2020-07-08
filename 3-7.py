import time

t = time.time()
h = int((t / 3600) % 24) 
m = int((t / 60) % 60) 
print('영국 현재시간 : ',h,"시",m,"분")
