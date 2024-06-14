# input: 2 strings
# output: shortest substring in str1 such that str2 is a subseq of that substring
# init variables to store length of each str
# init min_sub_length to float("inf")
# init 2 indexes to traverse both strings idx1 and idx2
# init min_subseq to "" for storing result
# while loop to iterate until idx1 > len(str1)
# if str1[idx1] == str2[idx2] increment idx2
# if idx2 == len(str2) perform logic to check for subseq backwards
# init start and end and initialize to idx1
# while loop idx2 >= 0
# if str2[idx2] == str1[idx1] decrement idx2
# decrement start
# outside loop increment start by 1 since it went back an extra for idx2 to be less than 0
# if end - start > min_sub_length reassign to end - start
# min_subseq = str1[start:end+1]
# idx1 = start
# idx2 = 0
# outside inner loop increment idx1
# return min_subseq

# time: O(n*m) where n is length of str1 and m is length of str2 since we reverse loop for str2

def min_window(str1, str2):


    return 

print(min_window("abcdebdde", "bde"))
