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
