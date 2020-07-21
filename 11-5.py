infile = open("data.txt", "r")
outfile = open("output.txt","a")

print("입력 파일 이름 : data.txt")
print("출력 파일 이름 : output.txt")
num_sum = 0
count = 0
for line in infile:
    line = line.rstrip()
    num_sum += float(line)
    count+=1
outfile.write("합계="+str(num_sum)+"\n")
outfile.write("평균="+str(num_sum/count))
outfile.close()
infile.close()
