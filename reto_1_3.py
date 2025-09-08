print("----Prime Number Checker----")

def is_prime(num: int) -> bool:
    # This function checks if a number is prime
    # It checks if the number is divisible by any number from 2 to the square root of the number
    if num <= 1:
        return False
    # We use int(num**0.5) + 1 to include the square root in the range
    for divisor in range(2, int(num**0.5) +1):
        if num % divisor == 0:
            return False
    return True

# We ask the user for how many numbers they want to enter
# And we create a list to store the prime numbers which the user provided
count: int = int(input("How many numbers do you want to check?: "))
prime_list = []

# We use a for loop to include the numbers in the list we created earlier
for number in range(count):
    num: int = int(input(f"{number + 1}°. "))
    if is_prime(num):
        prime_list.append(num)

print(f"The prime numbers you entered are: {prime_list}")