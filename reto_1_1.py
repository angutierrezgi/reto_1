print("----Basic Calculator----")

# We ask the user for two integers and and operation to perform
# We use a match-case, instead of if cases, to operate the two numbers

def calculator(var_1: int, var_2: int, operation: str) -> int:
    match operation:
        case "+":
            return var_1 + var_2
        case "-":
            return var_1 - var_2
        case "*":
            return var_1 * var_2
        case "/":
            while var_2 == 0:
                # We check if the second number is zero to avoid an error
                # If it is, we ask for another number instead
                # We use a while loop to keep checking until the user enter a non-zero number
                print("Cannot divide by zero. Enter another number.")
                var_2: int = int(input("Enter second number: "))
            return var_1 / var_2
        case _:
            # Default case if the operation is not one of the ones established beforehand
            print("INVALID OPERATION.")

var_1: int = int(input("Enter first number: "))
var_2: int = int(input("Enter second number: "))

operation: str = input("Enter operation (+, -, *, /): ")

result = calculator(var_1,var_2,operation)
print(f"{var_1} {operation} {var_2} = {result}")
