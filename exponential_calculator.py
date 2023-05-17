#Calculattion of exponential series

from Assignment_1.factorial import calculate_factorial_float as factorial
import math

class ExponentialCalculator :

    def calculate_exp(self, x, num_terms=5) :
        exp_sum = 0
        for i in range(num_terms):
            term = x**i/factorial(i)
            exp_sum += term
        return exp_sum

if __name__ == "__main__" :
    calculator = ExponentialCalculator()
    matriculation_no = 9
    exp_sum = calculator.calculate_exp(matriculation_no)
    print("Exponential sum is :", exp_sum)

    precision = 10**-12
    no_of_terms = 1
    approx_value = calculator.calculate_exp(matriculation_no, no_of_terms)
    exponential_value = math.exp(matriculation_no)

    error = abs(approx_value-exponential_value)
    while(error > 10**-12):
        no_of_terms += 1
        error = abs(calculator.calculate_exp(matriculation_no, no_of_terms)-math.exp(matriculation_no))
    print("Total no. of terms until error is less than 10*-12 is :", no_of_terms)












