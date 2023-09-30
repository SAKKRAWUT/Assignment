def serial_sum(*args):
    if len(args) == 1:
        return sum(range(1, args[0] + 1))
    elif len(args) == 2:
        return sum(range(args[0], args[1] + 1))
    else:
        raise ValueError("Function expects either 1 or 2 arguments, but got more.")


print(serial_sum(4))
print(serial_sum(2, 4))
