from ctypes import sizeof


numbers=[12,5,-1,31,-61,59,26,-53,58,97,-93,-23,84,-15,6]


def findSum(list):
    x = []
    while len(list) > 0:
        if len(x) == 0:
            x[0] = list[0]
        else:
            x.append(list())