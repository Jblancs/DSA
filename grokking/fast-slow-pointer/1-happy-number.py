# useful build-in python function - divmod gets whole number and remainder in a tuple

# create helper function to sum sq
# create total = 0
# while number > 0 (number = 0 when less than 10)
# unpack number and digit from divmod
# reassign total += digit squared
# return total

# input: number n
# output boolean if happy number (sum of sq = 1)
# create fast = sum_of_sq(n) and slow pointer
# while fast != 1 and slow != fast
# slow = sum_of_sq(slow)
# fast = sum_of_sq(sum_of_sq(fast))
# outside loop: if fast == 1 return true
# return false

# time: O(logn) since number with 3 digit 999 sum is 243 so 243 cycles is max
# space: O(1)


def is_happy_number(n):

    def sum_of_sq(number):
        total = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total += digit ** 2
        return total

    slow = n
    fast = sum_of_sq(n)

    while fast != 1 and slow != fast:
        slow = sum_of_sq(slow)
        fast = sum_of_sq(sum_of_sq(fast))

    if fast == 1:
        return True

    return False

print(is_happy_number(2147483646))
print(is_happy_number(19))
