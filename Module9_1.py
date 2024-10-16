def apply_all_func(int_list, *functions):
    results = {}

    for function_ in functions:
        results[function_.__name__] = function_(int_list)
    return  results

def start():
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

if __name__ == '__main__':
    start()