login = input("Enter your Login: ")

def decorator(func):
    def wrapper_decorator(*args, **kwargs):
        if login == "admin":
            value = func(*args, **kwargs)
            return value
        else:
            print("acess denied")
    return wrapper_decorator

@decorator
def your_balance():
    print("your balance is 5$")

your_balance()

