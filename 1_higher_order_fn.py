def before_after_hof(func):
    def wrap_func():
        print('BEFORE')
        func()
        print('AFTER')
    return wrap_func


def hello():
    print('Hello')


# Create the higher order function by passing our function as an argument
higher_order_fn = before_after_hof(hello)

# Call our new higher order function.
higher_order_fn()
