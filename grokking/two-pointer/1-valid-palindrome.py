# input: string s
# output: boolean for whether s is a palindrome
# time: On
# space: O1

def is_palindrome(s):

  point_a = 0
  point_b = len(s) - 1

  while point_a < point_b:
    if s[point_a] == s[point_b]:
      point_a += 1
      point_b -= 1
    else:
      return False

  return True

print(is_palindrome("kayak"))
print(is_palindrome("hello"))
