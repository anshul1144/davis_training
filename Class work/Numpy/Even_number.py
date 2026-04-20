# create a numpy array from the even factors of a given number.
import numpy as np

number = int(input("Enter a number: "))
if number < 0:
    factors = [i for i in range(-abs(number), 0) if number % i == 0 and i % 2 == 0]
elif number > 0:
    factors = [i for i in range(1, number + 1) if number % i == 0 and i % 2 == 0]
else:
    factors = [0]
even_factors_array = np.array(factors)
print("Even factors of the number:", even_factors_array)

