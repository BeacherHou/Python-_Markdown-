# 介绍sys模块



## 平台与版本

```python
>>> import sys
>>> sys.platform, sys.maxsize, sys.version
('linux', 9223372036854775807, '3.7.0 (default, Jun 28 2018, 13:15:42) \n[GCC 7.2.0]')
>>> if sys.platform == 'linux':
...     print('hello linux')
... 
hello linux
```

- sys.platform: 底层操作系统名称（**程序在不同的系统中表现出不同的行为**）
- sys.maxsize: 当前计算机可容纳的最大“原生”整型
- sys.version: Python解释器版本号



## 模块搜索路径

```python
>>> sys.path
['', '/home/alone/anaconda3/lib/python37.zip', '/home/alone/anaconda3/lib/python3.7', '/home/alone/anaconda3/lib/python3.7/lib-dynload', '/home/alone/anaconda3/lib/python3.7/site-packages']
```

- sys.path是一个由目录名称字符串组成的**列表**，代表正在运行的Python解释器的真正**搜索路径**
- sys.path是在解释器启动时根据以下内容进行初始化：
  - PYTHONPATH设置
  - Python目录下所有.pth路径文件的内容
  - 系统默认设置
- sys.path还包含了一个代表脚本主目录的指示器（空字符串，后面遇到os.getcwd时会详细介绍）和一组标准库目录
- sys.path也可以使用**列表方法**进行更改，但**仅维持到Python进程结束时**



## 已加载的模块表

```python
>>> sys.modules
{'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>, ...省略...
>>> sys
<module 'sys' (built-in)>
>>> sys.modules['sys']
<module 'sys' (built-in)>
>>> sys.getrefcount
<built-in function getrefcount>
>>> sys.getrefcount('sys')
91
>>> sys.builtin_module_names
('_abc', '_ast', '_codecs', '_collections', '_functools', '_imp', '_io', '_locale', '_operator', '_signal', '_sre', '_stat', '_string', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'atexit', 'builtins', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'posix', 'pwd', 'sys', 'time', 'xxsubtype', 'zipimport')
```

- sys.modules：一个字典，你的python进程所导入的每个模块
- sys.getrefcount()：一个函数，查看对象的引用次数
- sys.builtin_module_names：一个元组，Python可执行程序的内置模块名称



## 异常的详细信息

```python
>>> try:
...     raise IndexError
... except:
...     print(sys.exc_info())
... 
(<class 'IndexError'>, IndexError(), <traceback object at 0x7f1c568aa788>)
```

- sys.exc_info()会返回一个元组，其中包含有最近异常的类型、值和研究对象。这个调用返回的前两项打印时显示具有一定格式的字符串，第三项是一个追踪对象，可以用标准模块traceback处理
- 可以利用这些信息来格式化显示我们自己的错误信息

```python
>>> import traceback, sys
>>> def grail():
...      raise TypeError('already got one')
... 
>>> try:
...     grail()
... except:
...     exc_info = sys.exc_info()
...     print(exc_info[0])
...     print(exc_info[1])
...     traceback.print_tb(exc_info[2])
... 
<class 'TypeError'>
already got one
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in grail
```



## sys导出的其他常用工具

- sys.argv：显示为由字符串组成的列表的命令行参数
- sys.stdin, sys.stdout 和 sys.stderr：标准流
- sys.exit：强制退出程序