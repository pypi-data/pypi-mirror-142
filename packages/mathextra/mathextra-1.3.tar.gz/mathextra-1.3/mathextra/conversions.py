def decimal_to_binary(n):
    return bin(n).replace("0b", "")


def binary_to_decimal(n):
    stingn = str(n)
    for character in stingn:
        if character == '.':
            return 'Invalid'
        if character != 0 and character != 1:
            return 'Invalid'
    num = n
    dec_value = 0

    base = 1

    temp = num
    while temp:
        last_digit = temp % 10
        temp = int(temp / 10)

        dec_value += last_digit * base
        base = base * 2
    return dec_value


def deciamal_to_octadecimal(n):
    return oct(n)


def octadecimal_to_decimal(n):
    decimal_value = 0
    base = 1

    while (n):
        last_digit = n % 10
        n = int(n / 10)
        decimal_value += last_digit * base
        base = base * 8
    return decimal_value


def decimal_to_hexadecimal(n):
    return hex(n)
