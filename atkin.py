import math

# Class to generate prime numbers
class Atkin:
    limit = 100000000
    result = [0] * (limit + 1)
    primes = []

    def main(self):
        Atkin.result[2] = 1
        Atkin.result[3] = 1

        for i in range(1, int(math.sqrt(Atkin.limit))):
            for j in range(1, int(math.sqrt(Atkin.limit))):
                n = (4*i*i) + (j*j)
                if (n <= Atkin.limit and (n % 12 == 1 or n % 12 == 5)):
                    Atkin.result[n] = not Atkin.result[n]
                n = (3*i*i) + (j*j)
                if (n <= Atkin.limit and n % 12 == 7):
                    Atkin.result[n] = not Atkin.result[n]
                n = (3*i*i) - (j*j)
                if (n <= Atkin.limit and (n % 12 == 11) and ( i > j)):
                    Atkin.result[n] = not Atkin.result[n]

        for n in range(5, int(math.sqrt(Atkin.limit))):
            if (Atkin.result[n] == 1):
                x = 1
                while (x*n*n <= Atkin.limit):
                    Atkin.result[x*n*n] = 0
                    x += 1

        for n in range(0, Atkin.limit):
            if (Atkin.result[n] == 1):
                Atkin.primes.append(n)
