def hcf_finder(num1, num2):
    num1_factors = []
    num2_factors = []
    common_factors = []
    for i in range(num1 + 1):
        if i != 0 and num1 % i == 0:
            num1_factors.append(i)
    for i in range(num2 + 1):
        if i != 0 and num2 % i == 0:
            num2_factors.append(i)
    for i in range(len(num1_factors)):
        for n in range(len(num2_factors)):
            if num1_factors[i] == num2_factors[n]:
                common_factors.append(num2_factors[n])
    common_factors.reverse()
    return common_factors[0]


def hcf_finder_fast(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def lcm_finder(num1, num2):
    x = num1
    y = num2
    while y:
        x, y = y, x % y
    hcf = x
    lcm = (num1 * num2) // hcf
    return lcm


def factor_finder(number):
    output = []
    for i in range(number + 1):
        if i != 0 and number % i == 0:
            output.append(i)
    return output
