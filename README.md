# Prime Number Finder

This Python script allows you to find all prime numbers within a specified range. Prime numbers are natural numbers greater than one and have exactly two distinct positive divisors: 1 and the number itself.

## How to Use

1. **Run the Script**: Execute the script in a Python environment.
2. **Enter the Range**: You will be prompted to enter the lowest and upper range values.
3. **View Results**: The script will output all prime numbers within the specified range.

## Example

When you run the script, it will prompt you as follows:

```
The Prime numbers are defined as natural numbers greater than one and that have two distinct positive divisors
- dividing by 1
- dividing by the value of the number itself.
You can try it by yourself:

Please, Enter the Lowest Range Value:
```

Enter a value (e.g., `10`) and press Enter. Then it will prompt:

```
Please, Enter the Upper Range Value:
```

Enter a value (e.g., `50`) and press Enter. The script will then output:

```
The Prime Numbers in the range between 10 and 50 are:
11
13
17
19
23
29
31
37
41
43
47
```

## Code Explanation

1. **Description and Instructions**: The script starts by explaining what prime numbers are and instructing the user on how to use the script.
2. **User Input**: The script prompts the user to enter the lowest and upper range values.
3. **Input Validation**:
   - Checks if the lower value is equal to the upper value and informs the user if there are no numbers between them.
   - Checks if the lower value is greater than the upper value and informs the user if this is incorrect.
   - Checks if the upper value is just one more than the lower value and informs the user if there are no prime numbers between these values.
4. **Finding Prime Numbers**: If the input values are valid, the script finds and prints all prime numbers in the specified range.


## Dependencies

This script requires Python 3 to run.

## Contribute

If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue on the repository.