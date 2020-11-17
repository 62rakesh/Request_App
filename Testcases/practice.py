def multipliers():
    return [lambda x: i * x for i in range(7)]


print([m(9) for m in multipliers()])
