import pandas as pd
import inspect

def introspection_info(obj):
    type_ = type(obj).__name__
    attribute = getattr(obj, '__dict__', None)
    methods = dir(obj)
    module = obj.__class__.__module__
    func = inspect.isfunction(obj)
    info = {'type': type_, 'attributes': attribute, 'methods': methods, 'module': module, 'function': func}
    return info


if __name__ == '__main__':

    obj = pd.DataFrame({1: [3, 1, 2], 2: [5, 3, 4], 3: [7, 6, 5]})

    number_info = introspection_info(obj)
    print(number_info)