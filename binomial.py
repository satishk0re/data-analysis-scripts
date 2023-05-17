from factorial import calculate_factorial_float

class Binomial:
    def calculate_binomial_coefficient(self, n, k):
        a = n - k
        if n >= k and k != 0:
            numerator = calculate_factorial_float(n)
            denominator = calculate_factorial_float(k) * calculate_factorial_float(n-k)
            binomial = (numerator / denominator)
        else:
            binomial = 0
        return binomial
    def conduct_test(self):
        print(bi.calculate_binomial_coefficient(4, 2))
        print(bi.calculate_binomial_coefficient(10, 5))
        print(bi.calculate_binomial_coefficient(32, 20))


if __name__ == "__main__":
    bi = Binomial()
    bi.conduct_test()

""" The code is working fine for smaller numbers, but its giving floating value as a 
    output when we are using big numbers"""
