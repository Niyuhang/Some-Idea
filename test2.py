import requests
a = {'1': '2', '2': '4', '3': '6', '4': '8', '5': '10'}
print(a.__iter__())

# for i in a:
#     print(i)
#     a.pop(i)

def c():
    pass
print(c.__code__.co_flags)