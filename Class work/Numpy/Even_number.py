# create a numpy array from the even factors of a given number
import numpy as np

number = int(input("Enter a number: "))

even_factors = []

for i in range(1, number + 1):
    if number % i == 0:
        if i % 2 == 0:
            even_factors.append(i)

even_factors_array = np.array(even_factors)

print("Even factors are:", even_factors_array)