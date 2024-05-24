# input: sentence string
# output: sentence string in reverse

# helper function: reverse_str
# takes in string, starting idx, ending idx
# while start < end
# create start_value to store value to use after swapping
# reassign string[start] = string[end]
# reassign string[end] = start_value
# start += 1 and end -= 1
# return string

# create reversed_str variable and reverse sentence
# create str_len to store len(reversed string)
# create start and end pointer
# need nested loops
# while start < str_len
# while end < str_len && reversed_str[end] != " "
# end += 1
# outside nested loop perform logic
# call reverse_str(reversed_str, start, end - 1)
# start = end + 1
# end += 1
# outside loop return reversed_str

# time: O(n+n) or O(n) since string is traversed twice
# space: O(n) since we create a list for each char since python strings are immutable

import re

def reverse_words(sentence):
   sentence = re.sub(' +', ' ', sentence.strip())

   sentence = list(sentence)
   sentence.reverse()
   print(sentence)
   str_len = len(sentence) - 1


   start = 0
   end = 0

   while end <= str_len:
      if end == str_len or sentence[end] == " ":
         end_idx = (end - 1) if sentence[end] == " " else end
         reverse_str(sentence, start, end_idx)
         start = end + 1
      # print(f"start: {start} end: {end} str_len: {str_len}")
      end += 1

   return "".join(sentence)


def reverse_str(str, start, end):
   while start < end:
      str[start], str[end] = str[end], str[start]
      start += 1
      end -= 1
   return

print(reverse_words("We love Java "))
