# Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

# Your DynamicArray class should support the following operations:

# DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
# int get(int i) will return the element at index i. Assume that index i is valid.
# void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
# void pushback(int n) will push the element n to the end of the array.
# int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
# void resize() will double the capacity of the array.
# int getSize() will return the number of elements in the array.
# int getCapacity() will return the capacity of the array.
# If we call void pushback(int n) but the array is full, we should resize the array first.

class DynamicArray:

    def __init__(self, capacity: int):
        # time O(n) n = capacity
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        # time O(1)
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        # time O(1)
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # time O(n) if resized
        # average time O(1)
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        # time O(1)
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        # time O(n)
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr


    def getSize(self) -> int:
        # time O(1)
        return self.size

    def getCapacity(self) -> int:
        # time O(1)
        return self.capacity

# Example 1:

# Input:
# ["Array", 1, "getSize", "getCapacity"]

# Output:
# [null, 0, 1]
# Example 2:

# Input:
# ["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]

# Output:
# [null, null, 1, null, 2]
