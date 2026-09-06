username = "chaiaurcode"  # Global variable


def func():
    # username = "chai"  # Local variable if uncommented
    print(username)  # Reads global variable


print(username)
func()


x = 99  # Global variable


# def func2(y):
#     z = x + y  # Reads global x
#     return z


# result = func2(1)
# print(result)


# def func3():
#     global x  # Use global x
#     x = 12    # Modify global x


# func3()
# print(x)


# Enclosing scope / closure
def f1():
    x = 88

    def f2():
        print(x)  # Reads x from f1()

    return f2


myResult = f1()
myResult()


# Closure with parameter
def chaicoder(num):

    def actual(x):
        return x**num  # num comes from enclosing scope

    return actual


f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))


"""
Global   → variable outside functions
Local    → variable inside a function
global   → allows modifying a global variable
Enclosing → variable from an outer function
Closure  → inner function remembers outer variables
"""
