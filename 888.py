from dask.array.linalg import lstsq

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
lst = []
def recursive_flatten(arr):
    """
    Recursive algorithm
    Looks like recursive_flatten_iterator, but with extend/append

    """
    #lst = []
    for i in arr:
        if isinstance(i, list):
            lst.extend(recursive_flatten(i))
        elif isinstance(i, tuple):
            lst.extend(recursive_flatten(list (i)))
        else:
            lst.append(i)
    return lst

res = recursive_flatten(data_structure)
print(data_structure)
print(res)