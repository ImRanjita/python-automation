def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers_input = input("Enter numbers separated by commas: ")
numbers = [int(n.strip()) for n in numbers_input.split(",")]

print("The largest number is:", find_largest(numbers))