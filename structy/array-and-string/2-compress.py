# Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

# You can assume that the input only contains alphabetic characters.

# pseudo code:
# input: string
# output: a compressed string
# create 2 pointer variables to find each group of letters
# create result list (instead of string)
# use while loop to loop through each group until last index of s
# if index j is the same value of index i increment j
# else splice the group of letters and find the len then turn into string
# append len number if greater than 1 and value of index i
# set i = j
# join result list and return value

# time: O(n) because we loop through length of the string
# space: O(n)

def compress(s):
    # must add to get last group because while loop will end when j goes over len(s) (meaning it would skip the last group)
    s += '!'

    i = 0
    j = 0
    result = []

    while j < len(s):
        if s[j] == s[i]:
            j += 1

        else:
            num = j - i

            if num > 1: # only append number if there is more than one letter in a group
                result.append(str(num)) # turn into string in order to join

            result.append(s[i])
            i = j

    return "".join(result)

print(compress('ccaaatsss')) # -> '2c3at3s'
