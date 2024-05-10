# input: array of nums and target
# output: boolean whether 3 numbers from array sum to target amount
# time: sorting is O(nlogn) while nested loop is O(n^2) which simplifies to O(n^2)
# space: O(n) because of sort

def find_sum_of_three(nums, target):
    

list1 = [1,-1,0]
list2 = [3,7,1,2,8,4,5]
list3 = [3,7,1,2,8,4,5]

print(find_sum_of_three(list1,-1))
print(find_sum_of_three(list2,10))
print(find_sum_of_three(list3,21))
print(find_sum_of_three(
[-1, 2, 1, -4, 5, -3] , -8))
