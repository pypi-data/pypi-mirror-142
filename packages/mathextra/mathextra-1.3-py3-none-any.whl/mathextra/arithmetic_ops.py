def add(*args):
    output = 0
    for arg in args:
        output += arg
    return output


def subtract(*args):
    output = args[0]
    for num in range(len(args)):
        if num != 0:
            output -= args[num]
    return output


def multiply(*args):
    output = args[0]
    for num in range(len(args)):
        if num != 0:
            output *= args[num]
    return output


def divide(*args):
    output = args[0]
    for num in range(len(args)):
        if num != 0:
            output /= args[num]
    return output


def power(num1, num2):
    return pow(num1, num2)