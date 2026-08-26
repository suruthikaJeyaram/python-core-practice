'''Write the MathUtils class with the static calculateSum() method and provide
code to test the functionality.'''
class MathUtils:
    @staticmethod
    def sum_of_numbers(numbers):
        return sum(numbers)
result=MathUtils.sum_of_numbers([1,2,3,4,5])
print(result)