from collections import ChainMap

b = {'music': 'bach', 'art': 'rembrant'}
a = {'art': 'van gogh', 'opera': 'carmen'}
c = {'art': 'kiss', 'narch': 'rok'}
print(list(ChainMap(a, b, c)))


combined = b.copy()
combined.update(a)
combined.update(c)
print(list(combined))

