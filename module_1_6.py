my_dict = {"Ann": 1967, "Den": 1978, "Poul": 2001, "Soul": 1997}
print(my_dict)
print("Existing value: ", my_dict.get("Ann"))
print("Not existing value: ", my_dict.get("Debora"))
my_dict.update({"Nicke": 1985, "Lucy": 2002})
del_value = my_dict.pop("Den")
print("Deleted value: ", del_value)
print("Modified dictionary: ", my_dict)

my_set = {1, 2, 6, 6.7, 8, 2, "Parse",  True}
print("set", my_set)
my_set.add(12)
my_set.add("ggggggggggg")
my_set.discard(6.7)
print("Modified set: ", my_set)