# input: string s
# output: boolean for whether s is a palindrome
# time: On
# space: O1

def is_palindrome(s):
  left = 0
  right = len(s) - 1

  while left < right:
    if s[left] != s[right]:
      return False

    left += 1
    right -= 1

  return True

print(is_palindrome("kayak"))
print(is_palindrome("hello"))
