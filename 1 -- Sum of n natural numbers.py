def sum_of_natural_numbers(n):
   if n <= 0:
        return 0
   else:
        return n + sum_of_natural_numbers(n - 1)
n = int(input("Enter a positive integer: "))
if n < 0:
    print("Please enter a positive integer.")
else:
    result = sum_of_natural_numbers(n)

print(f"The sum of the first {n} natural numbers is: {result}")