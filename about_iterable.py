import collections
a = [1, 2, 3, 4]
b = {'1': 'hi', '2': 'hello'}
# print(isinstance(a, collections.Iterable))  # True
# print(isinstance(a, collections.Iterator))  # False



import dis
# dis.dis('for i in a:pass')

"""
iter(iterable) -> iterator
iter(callable, sentinel) -> iterator

Get an iterator from an object.  In the first form, the argument must
supply its own iterator, or be a sequence.
In the second form, the callable is called until it returns the sentinel.
有两种形式，都可以生成迭代器
"""
#1.
class B(object):
    res = [1, 2, 3, 4]
    def __init__(self):
        self.i = iter(self.res)

    def __call__(self):
        res = next(self.i)
        print("__call__ called, which would return ", res)


    # def __iter__(self):
    #     print('iter called')
    #     return iter(self.res)


class C(object):
    res = iter([1, 2, 3, 4])

    def __iter__(self):
        return self.res

    # def __next__(self):
    #     return next(self.res)
    #
    def __getitem__(self, item):
        print(item)
        return item
b = B()
I1 = iter(b, 5)
#第二个参数为限制值，当返回值为限制值的时候就停止
# print(next(I1))
# print(next(I1))
# print(next(I1))
# print(next(I1))

# print(slice(1, 3, [1, 2, 3, 4, 5]))
# print(isinstance(b, collections.Callable))
# print(isinstance(b, collections.Iterable))
# print(isinstance(I1, collections.Iterator))

c = C()

# print(isinstance(c, collections.Iterable))
# print(isinstance(c, collections.Iterator))
# print(isinstance(c, collections.Sequence))

li = [1, 2, 3, 4, 5]
a = li[slice(1, 3)]
print(a)
print(li[1:3])

c = [1, 2, 3, 4, 5]
d = iter(c)
for i in d:
    print(i)
    c.remove(i)