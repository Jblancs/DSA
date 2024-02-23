

# input strings s and t
# output: min window substring with shortest substring, same freq of each char as t
# init start = 0 for window
# init min_window_substring = ""
# init window = {} to hold char freq of window
# init req_count = {} to hold char freq of t
# init required to length of req_count
# init current to 0 to keep could of whether the required is met
# populate req_count with freq of each char and window with just each char with value of 0

def min_window(s, t):

    min_window_substring = [-1,-1]
    min_window_len = float("inf")
    window = {}
    req_count = {}

    for char in t:
        if char not in req_count:
            req_count[char] = 1
            window[char] = 0
        else:
            req_count[char] += 1

    current = 0
    required = len(req_count)
    start = 0

    for end in range(len(s)):
        char = s[end]

        if char in t:
            window[char] += 1

        if char in t and window[char] == req_count[char]:
            current += 1

        while current == required:

            if (end - start + 1) < min_window_len:
                min_window_len = (end - start + 1)
                min_window_substring = [start, end]

            if s[start] in t:
                window[s[start]] -= 1

            if s[start] in req_count and window[s[start]] < req_count[s[start]]:
                current -= 1

            start += 1
    start, end = min_window_substring
    res = s[start:end+1] if min_window_len != float("infinity") else ""
    return res


print(min_window("ABDFGDCKAB" , "ABCD"))
