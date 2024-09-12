def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

#print_params(a)
#print_params(a, b)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [1, "string", (1,2.3)]
values_dict = {
    "a": 45,
    "b": "name",
    "c": False
}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [25, "aero"]
print_params(*values_list_2, 42)