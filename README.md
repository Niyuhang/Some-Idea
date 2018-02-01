 # Some-Idea
 there is something new about what i learn
 # 1.Python 直接用，号分割元素就会变成元组
 例如 'aa','bbb'就是（'aa','bbb'）
 # 2.defaultdict使用
 初始化字典 a = defaultdict(xx) 传进来一个类型例如（dict）
 当使用 a[] 或 a.__setitem__()的不存在的key时 就会默认值为一个空字典
 >>> from collections import defaultdict
>>> a = defaultdict(dict)
>>> a['aa']
{} 
 # 3.metaclass的使用
 首先理解metaclass的概念，元类 就是创建类的一个类，元类本身也是类，然后type就是内置的一个元类， 使用__metaclss__或者（metaclass=xxx）
 来使用元类，class的时候，就会把 类名，bases父类，以及namespace等信息传到元类，让元类来进行创建类，如果本身没有这个属性，就会去父类找，模块等去找。
 
 ABCMeta 内置的抽象类，抽象类不能被实例化，抽象方法必须被重写，但是python的实现，要用metaclass=xx来实现，然后如果由abstractmethod装饰器，就无法被实例化。
在Python2中 可以使用__metaclass__ 来使用元类，但是在Python3当中使用方法变成class a（metalcass=xx）
可以利用six模块的 @six.add_metaclass装饰器来兼容Python2&3

 # 4.容器(container):容器是一种把多个元素组织在一起的数据结构，容器中的元素可以逐个地迭代获取，可以用in, not in关键字判断元素是否包含在容器中。
    就是能够存放元素的一个盒子。常见的list, set, dict 都是容器


 # 5.关于可迭代对象（iterable）,也就是我们所说的可迭代的对象,iterable被认为是一类对象，这类对象能够一次返回它的一个成员（也就是元素）。抽象一点就是适合迭代的对象。
    而它的本质其实是它能够返回一个迭代器。 通常在iterable中会实现一个__iter__ 或者 __getitem__的方法。一定有__iter__方法，而且返回值是一个迭代器.它更像是一个迭代器的接口.

    iterator,迭代器，可以被next()函数调用并不断返回下一个值的对象称为迭代器，迭代器是惰性的,一定要实现 __next__，和 __iter__方法

 当在python中使用for循环迭代一个对象时，调用者几乎分辨不出他迭代的是一个迭代器对象还是一个序列对象，因为python让他（迭代器）像一个序列那样操作。

 # 6.生成器(generator)
   生成器是迭代器的一种，
 # 7.iter, __iter__, next, __next__
   __next__:
   __iter__方法，定义在函数内部，返回一个迭代器







 # Git
 # 1.关于分支和pr
 克隆下来的仓库会默认是在master分支上，
 利用 git checkout -b xxx创建本地分支
     git checkout xxx 可以切换分支
     git branch -a 查看所有分支
切换到自己的分支后，修改相应代码，然后
git add . , git commit -m xxx 进行分支提交
如果切换回其它分支就会恢复到当前分支的代码情况
git push 把分支push上去
就可以提pr
