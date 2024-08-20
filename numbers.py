# Get start and end inputs from the user
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# Empty list to store odd and even numbers
odd_numbers = []
even_numbers = []

# loop to loop through each number in the specified range
for number in range(start, end + 1):
    if number % 2 != 0:
        odd_numbers.append(number)
    else:
        even_numbers.append(number)

print("Odd numbers between", start, "and", end, ":", odd_numbers)

print("Even numbers between", start, "and", end, ":", even_numbers)