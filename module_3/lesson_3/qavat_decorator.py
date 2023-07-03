


def decorator1(N):
    def inner(func):
        def wrapper(*args, **kwargs):
            response = N * func(*args, **kwargs)
            return response
        return wrapper
    return inner


def decorator2(N):
    def inner(func):
        def wrapper(*args, **kwargs):
            response = N * func(*args, **kwargs)
            return response
        return wrapper
    return inner

@decorator2(7)
@decorator1(2)
def test(nums_list):
    print(" enter test function")
    return nums_list


print(test(10))
# SUMMA



