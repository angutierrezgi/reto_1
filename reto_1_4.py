print("----Biggest Sum of Consecutive Numbers----")

count: int = int(input("How many numbers do you want to enter?: "))

# We create num_1 and biggest_sum variables outside the loop to keep their values
num_1: int = 0
biggest_sum: int = 0

# We create a for loop to go through the numbers the user wants to enter
# We interchange num__1 and num_2 to always have the last two numbers entered by the user
# We store the numbers and their sum if it's the biggest one so far
for number in range(count):
    num_2: int = int(input(f"{number + 1}°. "))
    sum: int = num_1 + num_2
    if sum > biggest_sum:
        # We also create two auxiliary variables to store the numbers which resulted in the biggest sum
        aux_1: int = num_1
        aux_2: int = num_2
        biggest_sum = sum
    num_1 = num_2

# Lastly, we print the auxiliary variables and the sum of them
print(f"The sum of {aux_1} and {aux_2} was the biggest, resulting in {biggest_sum}")