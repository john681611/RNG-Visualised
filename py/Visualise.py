def rngfunc():
    value = 0
    return value


def iterate(x=0, y=10000):
    arry = []
    for i in range(x,y):
        arry.append(rngfunc())
    return arry
