
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

    red = 0
    white = 0
    blue = len(colors) - 1

    if len(colors) == 1:
        return colors

    while white <= blue:
        if colors[white] == 0:
            if colors[red] != 0:
                colors[red], colors[white] = colors[white], colors[red]
            red += 1
            white += 1

        elif colors[white] == 1:
            white += 1

        else:
            if colors[blue] != 2:
                colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1

    return colors

print(sort_colors([0,1,0]))
print(sort_colors([1]))
print(sort_colors([1,1,0,2]))
