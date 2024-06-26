# input: string s of lowercase chars and integer k
# output: length of longest substring after replacing at most k chars
# init longest_len to -inf to store len of longest substring
# init start to track start of window
# init hash_map to store freq of each letter
# init most_freq_char to 0 for storing num of most freq char
# for end in len(s)
# if s[end] not in hash_map store it
# else increment s[end] += 1
# reassign most_freq_char to max(most_freq_char, hash_map[s[end]])
# let num_of_replacements = end - start + 1 - most_freq_char
# if num_of_replacements > k
# hash_map[s[start]] -= 1
# start += 1
# longest_len = max(end - start + 1, longest_len)

# time O(n) for each char
# space O(1) for hashmap with a max storing is 26 letters

def longest_repeating_character_replacement(s, k):
    string_len = len(s)
    len_of_max_sub = 0
    start = 0
    char_freq = {}
    most_freq_char = 0

    for end in range(string_len):
        if s[end] not in char_freq:
            char_freq[s[end]] = 1
        else:
            char_freq[s[end]] += 1

        most_freq_char = max(most_freq_char, char_freq[s[end]])

        if end - start + 1 - most_freq_char > k:
            char_freq[s[start]] -= 1
            start += 1

        len_of_max_sub = max(end - start + 1, len_of_max_sub)

    return len_of_max_sub




print(longest_repeating_character_replacement("aaacbbbaabab", 2))
