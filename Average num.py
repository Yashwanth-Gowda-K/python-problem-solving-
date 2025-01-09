def average_num(numbers):
    total = sum(numbers)
    count = len(numbers)

    avg = total / count

    return avg

numbers = (input("Enter the numbers by leaving the space: ").split()
)
numbers = [float (num) for num in numbers]
average = average_num(numbers)
print(f"Averge num is: {average}")