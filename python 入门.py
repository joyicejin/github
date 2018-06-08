# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:01:04 2017

@author: Administrator
"""

---
presentation:
  progress: true  
  slideNumber: true
  overview: true    
  transition: 'default' # none/fade/slide/convex/concave/zoom  
---

<!-- slide  vertical:true -->
## Python简明入门


<!-- slide  -->
<!-- toc depthFrom:1 depthTo:1-->

- [背景](#背景)
- [Python环境](#python环境)
- [Python简明入门](#python简明入门)

<!-- tocstop -->

<!-- slide  -->
# 背景

<!-- slide vertical:true -->
## 请用3个词语来概括Python？

<!-- slide vertical:true -->
## Python是什么
* 解释性的
* 面向对象的
* 带有动态语义的
* 编写的程序清晰易懂
* 简单
* 强大：胶水语言
* 开发速度快、运行速度慢

<!-- slide vertical:true -->
## Python哲学
* Beautiful is better than ugly.
* Explicit is better than implicit.
* Simple is better than complex.
* Complex is better than complicated.
* Flat is better than nested.
* Sparse is better than dense.
* Readability counts.
* Special cases aren't special enough to break the rules.
* Although practicality beats purity.

<!-- slide vertical:true -->
## Python哲学
* Errors should never pass silently.
* Unless explicitly silenced.
* In the face of ambiguity, refuse the temptation to guess.
* There should be one-- and preferably only one --obvious way to do it.
* Although that way may not be obvious at first unless you're Dutch.
* Now is better than never.
* Although never is often better than *right* now.
* If the implementation is hard to explain, it's a bad idea.
* If the implementation is easy to explain, it may be a good idea.
* Namespaces are one honking great idea -- let's do more of those!

<!-- slide  -->
# Python环境
* Python
  * Linux：自带
  * Windows：安装
* 包管理：Pip
  * 设置镜像
* IDE：PyCharm
* Anaconda
  * 包管理：conda

<!-- slide vertical:true -->
# Python简明入门

<!-- slide vertical:true -->
## 变量
* 没有类型
* 不需要声明，通过赋值=定义
* 不再使用的时候则会消失
```{python}
x = 10
y = 'abc'
z = True
```
* 多重赋值
```{python}
x, y = 1, 2
x = y = 1
```
<!-- slide vertical:true -->
## 语句块
* 注释#
* 通过并且只通过缩进表示
```{python id:"ixq33m5i"}
x = 1
if (x > 0):
    print('x is larger than zero')
```
* 逻辑表达式
  * False,[],0,"",None都表示逻辑假
  * 逻辑短路
```{python}
a = 1
b = 2
print(a or b)
print(a if a else b)
```
<!-- slide vertical:true -->
## 循环
```{python id:"ixq33r05"}
x = 1
while x <= 3:
    print(x, end=' ')
    x += 1
```
```{python id:"ixq33th8"}
for i in [1, 2, 3]:
    print(i, end=' ')
```
```{python id:"ixq33urg"}
for i in range(3):
    print(i + 1, end=' ')  
```

<!-- slide vertical:true -->
## 异常和断言
* 异常
```{python}
try:
    1 / 0
except Exception as ex:
    print(ex)
finally:
    print("finally")
```
* 断言
```{python}
import traceback

try:
    assert 1 == 0
except Exception as ex:
    traceback.print_exc()
```
<!-- slide vertical:true -->
## 用户输入
* input
```{python}
x = input("input a number:")
print(x)
print(type(x))
```
* 请输入12、abc、1+2试试

<!-- slide vertical:true -->
## 列表[]
* 定义
```{python}
['string1', 'string2']
[[1, 2], [2, 3, 4], [[]]]
```
* 索引
```{python id:"ixq3htch"}
x = [0, 1, 2, 3, 4]
print(x[2], end=' ')
print(x[-2], end=' ')
```
* 分片
```{python id:"ixq3isp6"}
x = [0, 1, 2, 3, 4]
print(x[1:3], x[2:], x[:2], x[:], end=' ')
```

<!-- slide vertical:true -->
## 元组()
* 不可变的列表

<!-- slide vertical:true -->
## 字典
* 定义
```{python}
age = {'rose': 30, 'shaw': 40}
```

* 索引
```{python id:"ixq3m84p"}
age = {'rose': 30, 'shaw': 40}
print(age['rose'])
```

<!-- slide vertical:true -->
## 函数
* 定义函数
```{python}
def double(x):
    return 2 * x
```
* 值参
```{python id:"ixpjdaa7"}
def double(x):
    x = 2 * x

x = 1
double(x)
print(x)
```

<!-- slide vertical:true -->
## 函数
* 可以改变参数的内容
```{python id:"ixq4g80a"}
def double(x):
    if (isinstance(x, list)):
        for i in range(len(x)):
            x[i] *= 2
    else:
        raise Exception("x not a list")
def trydouble(y):
  try:
      double(y)
  except Exception as ex:
      print("Exception:", ex)
  print(y)
trydouble(1)
trydouble([1,2])
```

<!-- slide vertical:true -->
## 函数
* 关键字参数
```{python id:"ixq4ff2j"}
def double(x, doublerate=2):
    return doublerate * x
print(double(1,doublerate=3))
```

* 函数本身是一种变量
```{python id:"ixq3pvbm"}
def double(x):
    return 2 * x
anotherdouble = double
print( anotherdouble(1))
```

<!-- slide vertical:true -->
## 对象
```{python id:"ixq3zcqm"}
class Contents:
    def __init__(self, contents=None):
        self.contents = contents or []

    def add(self, element):
        self.contents.append(element)

    def print_me(self):
        result = ""
        for element in self.contents:
            result += " " + repr(element)
        print("contents:" + result)
#逻辑短路

contents = Contents()
contents.add(123)
contents.add('abc')
contents.print_me()
```

<!-- slide vertical:true -->
## 对象
* 继承（支持多重继承）
```{python id:"ixq6hfkl"}
class Phone:
    def __init__(self):
        print("Phone")

class Camera:
    def __init__(self):
        print("Camera")

class XiaoMiMax(Phone, Camera):
    pass

myPhone = XiaoMiMax()
```

<!-- slide vertical:true -->
## 模块
```{python}
import math
print(math.sqrt(4))

from math import sqrt
print(sqrt(4))
```
