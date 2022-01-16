def send_error_data(func):
    def wrap_func():
        try:
            func()
        except Exception as e:
            print('Capture error here')
            # capture_error(e)
            # Again raise the exception
            raise e

    return wrap_func


@send_error_data
def fn_that_fails():
    raise Exception("Sorry, this failed")


fn_that_fails()
