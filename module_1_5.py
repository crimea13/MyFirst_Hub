immutable_var = (1, 6, "string", True, 5.7, "house")
print(immutable_var)
# TypeError: 'tuple' object does not support item assignment
mutable_list = [5, "fffffff", False, 8.0, 55, "bool"]
mutable_list[2] = "ggggggggggg"
print(mutable_list)