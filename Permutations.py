from itertools import permutations

mylist = [1, 2, 3, 4, 5, 6, 7]
list_of_permutations = permutations(mylist)
cnt = 0
for permutation in list_of_permutations:
    cnt += 1
print(len(mylist), cnt)