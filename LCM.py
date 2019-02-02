from math import gcd


# longest common multiple for finding hyper periods
def LCM(input):
    # lcm = float(0)
    lcm = input[0]
    for i in input[1:]:
        lcm = int(lcm*i/gcd(lcm, i))
    return lcm

