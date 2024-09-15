data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
total_sum = 0
def sum_numbers_and_string_lengths(data):
    #total_sum = 0
    sum_element(data)
    return total_sum

def sum_element(element):
    global total_sum
    #nonlocal total_sum
    if isinstance(element, int):
        total_sum += element
    elif isinstance(element, str):
        total_sum += len(element)
    elif isinstance(element, (list, tuple, set)):
        for item in element:
            sum_element(item)
    elif isinstance(element, dict):
        for key, value in element.items():
            sum_element(key)
            sum_element(value)



result = sum_numbers_and_string_lengths(data_structure)

print(f"Сумма чисел и длин строк: {result}")
