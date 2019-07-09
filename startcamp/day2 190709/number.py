# number.txt를 읽어서
with open('number.txt','r') as f:
    numbers=f.readlines()

print(numbers)

# 리스트를 뒤집는다.
numbers.reverse()

print(numbers)
with open('number_Reverse2.txt','w') as file:
    for number in numbers:
        file.write(number)

# number_reverse.txt로 저장
# with open('number_reverse.txt','w') as file:
#     for i in range(len(numbers)):
#         file.write(numbers[len(numbers)-i-1])

# 4
# 3
# 2
# 1
# 0