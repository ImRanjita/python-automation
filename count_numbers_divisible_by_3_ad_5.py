
count = 0
for numbers in range(1, 100):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print(numbers)
        count += 1
print("Total numbers divisible by 3 and 5:", count)