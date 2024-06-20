# a = int(input("enter first number: "))
# def mul(a):
#     def helper(b):
#         return a*b
#     return helper
# b = int(input("enter second number: "))
# mul_5 = mul(a)
# print(mul_5(b))

# import datetime

# def date_logger(fun):
#     def helper1(v):
#         return str(datetime.datetime.now()) + " " + str(v)
#     return helper1

# func = date_logger(min)
# print(func([1, 2, 3]))

def check_len(func):
    def wrapper_decorator(*args, **kwargs):
        if len(args[0]) > 5:
            return "too many"
        value = func(*args, **kwargs)
        value = value/2
        return value
    return wrapper_decorator

@check_len
def my_len(lst):
    return len(lst)


a = my_len([1, 2, 3])
print(a)