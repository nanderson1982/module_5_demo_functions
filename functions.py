"""
Description: Module 05 demonstration: Functions
Author: {student name}
Date: {current date}
Usage: To run individual functions, place a function 
call within the main guard.
"""


def greet() -> None:
    """
    Prints a greeting message to the console.
    Returns: None
    """

    print('Hello, world!')


#greet()
#greet()


#def greet_name(name): # Does not meet PEP8 standards

def greet_name(name: str) -> None:  # This meets PEP8 standards
    """
    Prints a greeting which includes the value of the name argument.
    Args: name (str): The name of the person to greet.
    Returns: None
    """

    print(f'Hello, {name}!')

#greet_name(name = "Poop")
#greet_name("Annie")


def greet_name_age(name: str, age: int) -> None:
    """
    Prints a greeting which includes the values of name and age arguments.
    Args:
        name (str): The name of the person to greet
        age (int): The age of the person to greet
    Returns:
        None
    """

    print(f"Hello {name}, you are {age} years old.")

#greet_name_age(name = 'John', age = 20)



def math_operation(operand1: int, operand2: int, operation: str) -> float:
    """
    Returns the results of the specified operation based on the two operands.
    Args:
        operand1 (int): The first operand.
        operand2 (int): The second operand.
        operation (str): The operation to perform.
    Retuns: float
    Raises: 
        ValueError: "Invalid operation. When operation is not + or -."
    """

    if operation == "+":
        result = operand1 + operand2
    elif operation == "-":
        result = operand1 - operand2
    else:
        raise ValueError("Invalid operation.")

    return result

try:
    result = math_operation(1, 3, "*")
except ValueError as e:
    print(e)


#print(math_operation.__doc__) # __ is called dunder

#print(input.__doc__)
#print(len.__doc__)

