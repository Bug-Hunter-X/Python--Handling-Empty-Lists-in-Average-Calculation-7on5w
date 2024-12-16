def calculate_average(numbers):
    if not numbers:  # Check for empty list
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

# Additional example to show robustness:
my_list_with_zero = [0,0,0]
average_zero = calculate_average(my_list_with_zero)
print(f"The average of a list with only zeros is: {average_zero}") 