class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = []
        counter = 0
        number = 0

        prime_factors = [2, 3, 5]

        while counter < n:
            ugly_numbers.append(False)
            number += 1

            if number == 1:
                ugly_numbers[number-1] = True
                counter += 1

            else:
                for prime_factor in prime_factors:
                    if number % prime_factor == 0:
                        if ugly_numbers[number // prime_factor - 1]:
                            ugly_numbers[number - 1] = True
                            counter += 1
                            break

        return number
