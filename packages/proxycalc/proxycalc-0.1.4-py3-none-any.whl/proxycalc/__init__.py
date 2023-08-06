"""
    Proxycalc provides a Calculator class for handling basic mathematical
    operations.
"""

__version__ = "0.1.4"


class Calculator:

    """
    Creates an object with an initialized value of zero, on which various mathematical operations can be done.

    Get object value by calling the "value" property.

    This calculator does not handle complex number computations.
    """

    def __init__(self, initial_value= 0):
        if not isinstance(initial_value, int) and not isinstance(initial_value, float):
          print("Calculator object can only be initialized with integer or float types.")
          return
        self.value = initial_value

    def reset(self):
        self.__init__()

    def find_root(self, index):
        """
        Finds the nth root of the value of the Calculator object, where n is the index parameter.

        Receives only one argument, index which is the inverse power of the root.

        Does not allow for index of multiple of 2 object value if negative
        """
        try:
            if self.value < 0 and not index % 2:
                print(
                    f'Can not find the {index}{"nd" if not (index - 2) % 10 else "th"} root of a negative value.'
                )
                return
            self.value = self.value ** (1 / index)
        except TypeError:
            print(
                "Can not run mathematical expressions on non-integer or non-float types"
            )
        except ZeroDivisionError:
            print("Attempting to use an expression that involves dividing by zero")

    def add(self, *numbers):
        """
        Adds an infinite number of integers, or floating point numbers, to the value of Calculator object .

        Can receive any number of arguments.
        """
        try:
            k = sum(numbers)
            if isinstance(k, complex):
                print(
                    "You provided a complex number and the calculator only handles real numbers"
                )
                return
            self.value += k
        except TypeError:
            print("Can not add non-float or non-integer types")

    def subtract(self, *numbers):
        """
        Subtracts an infinite number of integers, or floating point numbers, to the value of Calculator object .

        Can receive any number of arguments.
        """
        try:
            k = sum(numbers)
            if isinstance(k, complex):
                print(
                    "You provided a complex number and the calculator only handles real numbers"
                )
                return
            self.value -= k
        except TypeError:
            print("Can not do a subtract on non-float or non-integer types")

    def multiply_by(self, number):
        """
        Multiplies the value of Calculator object by a specific number .

        Receives just one argument which should be either integer or float.
        """
        try:
            if isinstance(number, complex):
                print(
                    "You provided a complex number and the calculator only handles real numbers"
                )
                return
            self.value *= number
        except TypeError:
            print("Can not do a mulitiplication on non-float or non-integer types")

    def divide_by(self, number):
        """
        Divides the value of Calculator object by a specific number .

        Receives just one argument which should be either integer or float and also non-zero.
        """
        try:
            if isinstance(number, complex):
                print(
                    "You provided a complex number and the calculator only handles real numbers"
                )
                return
            self.value /= number
        except TypeError:
            print("Can not do a division on non-float or non-integer types")
        except ZeroDivisionError:
            print("Attempting to divide by zero is not allowed.")
