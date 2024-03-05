# input: src, dst, words list
# output: length of sequence

# init a word_set to hold the list of words for O(1) check
# edge case: if src not in word_set return 0
# init queue to perform iterations on
# init counter to count length of sequence
# while loop to iterate while queue has a value
# increment counter by 1
# init length_of_queue equal to to hold how many values were added to the queue in one check
# use for loop to iterate over each of the values added in that round
# init current to popleft of queue
# for loop to iterate over each current_idx of the current
# init alpha to letters of the alphabet abcdefghijklmnopqrstuvwxyz
# for char in alpha
# init temp to list(current)
# reassign temp[current_idx] equal to char
# join list into a string
# if temp == dst return length + 1
# if temp in word_set append word to queue and remove from the set

from collections import deque

def word_ladder(src, dest, words):
    word_set = set(words)

    if dest not in word_set:
        return 0

    queue = deque([src])
    seq_counter = 0

    while queue:
        seq_counter += 1
        length_of_queue = len(queue)

        for _ in range(length_of_queue):
            current = queue.popleft()

            for current_idx in range(len(current)):
                alpha = "abcdefghijklmnopqrstuvwxyz"

                for char in alpha:
                    temp = list(current)
                    temp[current_idx] = char
                    temp = "".join(temp)

                    if temp == dest:
                        return seq_counter + 1

                    if temp in word_set:
                        queue.append(temp)
                        word_set.remove(temp)

    return 0
