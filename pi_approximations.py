#Calculation of pi approximations

def calculate_pi_initial(initial):
    pi_sum = 0
    sign = 1
    for num in range (initial):
        term = sign/((2*num+1)*3**num)
        pi_sum += term
        sign *= -1
    return 12**0.5*pi_sum

def calculate_pi_alternative(alternative):
    pi_1sum = 0
    sign_1 = 1
    for num_1 in range (alternative):
        term_1 = sign_1/(2*num_1+1)
        pi_1sum += term_1
        sign_1 *= -1
    return 4*pi_1sum

if __name__ == "__main__" :
    print("The value of pi from equation 1 is", calculate_pi_initial(100))
    print("The value of pi from equation 2 is", calculate_pi_alternative(100))

#5)
"""The initial method is relatively more efficient as it converges to pi 
value relatively faster to alternative method.
, In a nutshell it's computationally more efficient."""