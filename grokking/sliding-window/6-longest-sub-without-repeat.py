# input: str
# output: length of longest substring without repeat
# init hash for tracking if window contains repeating character
# init char_idx to store idx of current char
# init start to 0 to store window
# init result to array of 2 idx
# init res_len to len(result)

# for loop to iterate until end of str
# if str[end] not in hash then add it with the idx as value
# else repeat char is found
# if the length of the current window > res_len reassign result to [start,end]
# reassign res_len to end - start + 1
# reassign start to hash[str[end]] + 1 to start after the first repeat char
# outside loop return substring str[result[0], result[1] + 1]

# time: O(n) n being each char and m checking hashmap and removing

def find_longest_substring(input_str):
    if len(input_str) == 0:
        return 0

    hash = {}
    start = 0
    window_len = 0
    longest = 0

    for idx, val in enumerate(input_str):
        if val not in hash:
            hash[val] = idx

        else:
            if hash[val] >= start:
                window_len = idx - start
                if longest < window_len:
                    longest = window_len
                start = hash[val] + 1
            hash[val] = idx

    idx += 1
    if longest < idx - start:
        longest = idx - start

    return longest

print(find_longest_substring("abcdbea"))
