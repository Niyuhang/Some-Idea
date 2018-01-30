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
