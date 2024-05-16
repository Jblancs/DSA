
# Given an array, colors, which contains a combination of the following three elements:

# 0 (representing red)
# 1 (representing white)
# 2 (representing blue)

# Sort the array in place so that the elements of the same color are adjacent, with the colors in the order of red, white, and blue.

# input: colors list
# output: sorted list
# create red, white and blue pointer
# while white != blue
# if colors[white] == 0 swap red and white and increment both
# if colors[white] == 1 increment white
# if colors[white] == 2 swap white and blue and decrement blue
# outside loop return colors

# time: O(n) since we traverse once
# space: O(1)

def sort_colors(colors):


    return colors

print(sort_colors([0,1,0]))
print(sort_colors([1]))
print(sort_colors([1,1,0,2]))
