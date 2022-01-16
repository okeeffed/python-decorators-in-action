def before_after_hof(func):
    def wrap_func():
        print('BEFORE')
        func()
        print('AFTER')
    return wrap_func


@before_after_hof
def hello():
    print('Hello')


# Call our hello function
hello()
