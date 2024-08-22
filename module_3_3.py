def print_params(a=1, b="строка", c=True):
    print(a, b, c)

print_params()
print_params(10)  # a
print_params(b=25)  # b
print_params(c=[1, 2, 3])  # c

values_list = [1.12, "Егор", True]
values_dict = {"a": 24, "b": "текст", "c": False}

print_params(*values_list,)
print_params(**values_dict)
values_list_2 = [54.32, "строки"]
print_params(*values_list_2, 42)
