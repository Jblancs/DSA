# input: 2 integers
# output: number in string format with repetitive decimal in parentheses

# edge case: if numerator is 0 return 0
# init result to empty string to store string
# if either numerator or denominator is negative add "-"
#
def fraction_to_decimal(numerator, denominator):
    result, remainder_map = "", {}
    if numerator == 0:
        return '0'

    if (numerator < 0) ^ (denominator < 0):
        result += '-'

        numerator = abs(numerator)
        denominator = abs(denominator)

    quotient = numerator / denominator
    remainder = (numerator % denominator) * 10
    result += str(int(quotient))

    if remainder == 0:
        return result
    else:

        result += "."
        while remainder != 0:

            if remainder in remainder_map.keys():
                beginning = remainder_map.get(remainder)
                left = result[0:beginning]
                right = result[beginning: len(result)]
                result = left + "(" + right + ")"
                return result

            remainder_map[remainder] = len(result)
            quotient = remainder/denominator
            result += str(int(quotient))
            remainder = (remainder % denominator) * 10

        return result
