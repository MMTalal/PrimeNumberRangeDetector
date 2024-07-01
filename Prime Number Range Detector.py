# Print a description of prime numbers and instructions for the user
print("The Prime numbers are defined as natural numbers greater than one and that have two distinct positive divisors\n- dividing by 1 \n- dividing by the value of the number itself.\nYou can try it by yourself:\n\n")

# Prompt the user to enter the lowest range value
lower_value = int(input("Please, Enter the Lowest Range Value: "))

# Prompt the user to enter the upper range value
upper_value = int(input("Please, Enter the Upper Range Value: "))

# Check if the lower value is equal to the upper value
if lower_value == upper_value:
    print("There are no numbers between them, please try again")

# Check if the lower value is greater than the upper value
elif lower_value > upper_value:
    print("The lower value is bigger than the upper value! .. this is incorrect, please try again")

# Check if the upper value is just one more than the lower value
elif upper_value == (lower_value + 1):
    print(f"There are no prime numbers between {lower_value} and {upper_value}. Maybe you can try another range.")

# If the input values are valid, proceed to find and print prime numbers in the range
else:
    print(f"The Prime Numbers in the range between {lower_value} and {upper_value} are:")

    # Iterate over each number in the specified range
    for number in range(lower_value, upper_value + 1):
        # Check if the number is greater than 1 (as primes are greater than 1)
        if number > 1:
            # Check if the number is divisible by any number from 2 to number-1
            for i in range(2, number):
                if (number % i) == 0:
                    break  # If it is divisible, it is not a prime number, exit the loop
            else:
                # If not divisible by any number, it is a prime number, print it
                print(number)
