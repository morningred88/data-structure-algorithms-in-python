class FactorialUsingRecursion:
    """
    This class demonstrates the factorial of a given number using recursion
    """

    def fact(self, number):

        # Base case
        if number == 0:
            return 1
        else:
            return number * self.fact(number-1)


factorial = FactorialUsingRecursion()
print(factorial.fact(5))

