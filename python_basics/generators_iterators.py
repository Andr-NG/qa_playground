itr = (i for i in range(3))
print(next(itr))
print(next(itr))
print(next(itr))

# raises StopIteration because it can interated over only once
print(next(itr))