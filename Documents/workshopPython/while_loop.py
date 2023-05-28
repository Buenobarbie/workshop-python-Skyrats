i = 1
while i < 6:
    print(i)
    i += 1


num = 128
count = 0

while True:
    num /= 2
    count += 1
    if(num == 1):
        break

print(count) # 7