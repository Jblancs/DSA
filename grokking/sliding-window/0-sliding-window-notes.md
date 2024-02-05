# Sliding Window

## Pattern

Pattern is used to process sequential data by maintaining a moving subset of elements, called a window. Aimed at reducing the use of nested loops in algorithm.

**Window:** Used to slide over the data in chunks corresponding to the window size. Allows us to process data in segments instead of the entire list.

## Does my problem match this pattern?

**Yes if:**
- Problem requires repeated computation on contiguous set of data elements (subarray or substring).
- The computations performed every time window moves take O(1) or are slow growing functions such as log

**No if:**
- input data structure does not support random access
- You have to process entire data set without segentation

## Real World Problems
- **Telecommunications:** Find max users connected to cellular network's data station
- **E-Commerce:** Given data set of product IDs in the order they were viewed byy user and list of products likely to be similar, find how many times these products occur together
- **Video streaming:** Given stream of numbers representing number of buffering events, calculate median number of buffering events in 1 minute interval
- **Social media content mining:** Given lists of topics 2 users have posted about, find the shortest sequence of posts by one user that includes all topics that other users have posted about

