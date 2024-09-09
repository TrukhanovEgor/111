
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


# Вызовем test_function
test_function()


try:
    inner_function()
except NameError as e:
    print(f"Ошибка: {e}")
