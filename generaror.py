# def my_gen():
#     yield "monia"
#     yield "bruno"
#     yield "marti"
    
# g = my_gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

my_list = [1, 2, 5, 65,[13, 8,[7, 2], 3], 7 ,8]
def rek(some_list):
    for el in some_list:
        if isinstance(el, list):
            rek(el)
        else:
            print(el)
            
rek(my_list)
