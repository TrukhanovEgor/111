def calculate_structure_sum(data):
    total = 0

    if isinstance(data, (list, tuple)):
        for item in data:
            total += calculate_structure_sum(item)

    elif isinstance(data, dict):
        for key, value in data.items():
            total += calculate_structure_sum(key)
            total += calculate_structure_sum(value)

    elif isinstance(data, str):
        total += len(data)

    elif isinstance(data, (int, float)):
        total += data

    return total


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 6},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{'Urban': 'Urban2', 2: 35}])
]

result = calculate_structure_sum(data_structure)
print(result)
