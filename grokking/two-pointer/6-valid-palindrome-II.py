# input: string
# output: boolean whether it can be palindrome by removing 1 char
# create left and right pointers
# create counter = 0
# while loop to iterate while left < right
# if s[left] != s[right]:
# if counter == 0: left += 1 and counter += 1
# if counter == 1: left = 0, right = 0, counter += 1 continue
# if counter == 2: right -= 1 and counter += 1
# if counter == 3: return False
# left += 1
# right -= 1
# outside loop return True

def is_palindrome(s):

  left = 0
  right = len(s) - 1
  counter = 0

  while left < right:
    if s[left] != s[right]:
        if counter == 0:
           left += 1
           counter += 1
           continue
        elif counter == 1:
           left = 0
           right = len(s) - 1
           counter += 1
           continue
        elif counter == 2:
           right -= 1
           counter += 1
           continue
        elif counter == 3:
           return False

    left += 1
    right -= 1

  return True

print(is_palindrome("madame"))
print(is_palindrome("tebbem"))
