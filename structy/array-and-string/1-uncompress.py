# Write a function, uncompress, that takes in a string as an argument.
# The input string will be formatted into multiple groups according to the following pattern:

# <number><char>

# for example, '2c' or '3a'.

# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively.
# You may assume that the input string is well-formed according to the previously mentioned pattern.


# pseudo code:
# input: string
# output: uncompressed version of string
# create list for result since append is O(1) (not using variable because concat in python is not O(1))
# create numeric string to see if an idx is a number
# create 2 pointer variables (i and j) to track any multi digit numbers
# use a while loop to loop through each index of s as long as j pointer is less than string length
# if statement for if idx j is a number add +1 to j
# else (idx j is not a number) append idx j of s * sliced portion from i-j(non incl)
# also increment j +1 to move onto the next group and let i = j
# return "".join(result) (since concat is not in loop it has better time comp)
# time: O(nm) since concat is not nested within while loop
# space: O(nm) since we need to build string


def uncompress(s):
    numeric = '0123456789'
    result = [] # appending is O(1) time comp
    i = 0
    j = 0

    while j < len(s):
        if s[j] in numeric:
            j += 1
        else: # s[j] is a letter
            num = int(s[i:j]) # slice out the number (non inclusive)
            result.append(s[j] * num)
            j += 1 # move to next group
            i = j # catch i up to current group

    return "".join(result)




uncompress("2c3a1t"); # -> 'ccaaat'
uncompress("10y"); # -> 'yyyyyyyyyy'
