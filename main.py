r = ['a', 'b', 'a', 'd']
rs = list(map(lambda y: y[0], list(filter(lambda x: x[1] == 'a', enumerate(r)))))
print(rs)