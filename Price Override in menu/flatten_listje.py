import more_itertools


lst = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]

FL = list(more_itertools.flatten(lst))
print(FL)
