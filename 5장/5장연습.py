# def varfun(*args) :
#     print(args)

# print("하나의 값으로 호출")
# varfun(10)
# print("여러 개의 값으로 호출")
# varfun(10, 20, 30)

# def myfunc(**kwargs) :
#     result = ""
#     for arg in kwargs.values() :
#         result += arg
#     return result

# print(myfunc(a = "Hi!", b = "Mr.", c = "kim"))

# def sum(a, b, c) :
#     print(a + b + c)

# alist = [1, 2, 3]
# sum(*alist)

# gx = 100

# def myfunc() :
#     global gx
#     gx = 200
#     print(gx)
# myfunc()
# print(gx)