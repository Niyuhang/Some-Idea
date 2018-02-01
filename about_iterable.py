import collections

# iterable ex
a = [1, 2, 3, 4]
# print(isinstance(a, collections.Iterable))  # True

class test_iterable():
    def __iter__(self):
        pass


test = test_iterable()
# print(isinstance(test, collections.Iterable))


#======================================================华丽的分割线=====================================================

class test_iterator():

    def __iter__(self):
        pass

    def __next__(self):
        print('111')

test = test_iterator()

# next(test)
# print(isinstance(test, collections.Iterator))


#======================================================华丽的分割线=====================================================
c = [1, 2, 3, 4, 5]

# for i in c:
#     print(i)
#     c.remove(i)

#======================================================华丽的分割线=====================================================

import dis
# dis.dis('for i in a:pass')

'''
  1           0 SETUP_LOOP              14 (to 17)
              3 LOAD_NAME                0 (a)
              6 GET_ITER
        >>    7 FOR_ITER                 6 (to 16)
             10 STORE_NAME               1 (i)
             13 JUMP_ABSOLUTE            7
        >>   16 POP_BLOCK
        >>   17 LOAD_CONST               0 (None)
             20 RETURN_VALUE

'''

#======================================================华丽的分割线=====================================================

"""
iter(iterable) -> iterator
iter(callable, sentinel) -> iterator

有两种形式，都可以生成迭代器
"""

class B(object):
    res = [1, 2, 3, 4]

    def __init__(self):
        self.i = iter(self.res)

    def __call__(self):
        res = next(self.i)
        print("__call__ called, which would return ", res)
        return res

    def __iter__(self):
        print('iter called')
        return self.i

b = B()
# I1 = iter(b)
# I2 = iter(b, 5)
for x in b:
    print(x)

# print(I1)
# print(I2)
# print(next(I2))
# print(next(I2))
# print(next(I2))
# print(next(I2))
#第二个参数为限制值，当返回值为限制值的时候就停止


#======================================================华丽的分割线=====================================================

#生成器ex
#1
def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

# f = fib()
#
generator_flag = 1 << 5
print(fib.__code__.co_flags & generator_flag)

# print(f.gi_frame.f_lasti)
#
#
# print(fib())
# print(next(f))

#2
# d = (i for i in range(10))
# print(d)
# for i in d:
#     print(i)

def fib2():
    a, b = 0, 1
    while True:

        a, b = b, a+b
def a():
    pass

print(a.__code__.co_flags)