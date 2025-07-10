start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

def sum_range(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

print(sum_range(start, end))