

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
    if t == "":
        return ""

    window = {}
    req_count = {}

    for c in t:
        req_count[c] = 1 + req_count.get(c, 0)

    for c in t:
        window[c] = 0

    current, required = 0, len(req_count)
    res, res_len = [-1, -1], float("infinity")
    left = 0

    for right in range(len(s)):
        c = s[right]

        if c in t:
            window[c] = 1 + window.get(c,0)

        if c in req_count and window[c] == req_count[c]:
            current += 1

        while current == required:
            if (right - left + 1) < res_len
                res = [left, right]
                res_len = (right - left + 1)

            if s[left] in t:
                window[s[left]] -= 1

            if s[left] in req_count and window[s[left]] < req_count[s[left]]:
                current -= 1

            left += 1

    left, right = res

    return s[left:right+1] if res_len != float("infinity") else ""


print(min_window("ABDFGDCKAB" , "ABCD"))
