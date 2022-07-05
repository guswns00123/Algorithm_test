import sys

#영화제목
num = int(input())
count = 0
string = 666
while True:
    if "666" in str(string): count +=1
    if count == num:
        break
    
    string+=1

print(string)