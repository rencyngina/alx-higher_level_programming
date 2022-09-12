afe_print_division(a, b):
    div = 0
    try:
        div = a/b
        return div
    except ZeroDivisionError:
        div = None
    finally:
        print("Inside result: {}".format(div))
