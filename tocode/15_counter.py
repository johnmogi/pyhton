import collections

c = collections.Counter()

c.update({1,1,1, 2, 3, 1, 2, 3, 1, 2})

print(c)
print(c.most_common())