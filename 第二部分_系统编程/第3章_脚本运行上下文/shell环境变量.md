# *shell*环境变量

*shell*变量有事称之为环境变量，*Python*脚本可以通过一个类似*Python*字典的对象`os.environ`来访问它们。



## 获取*shell*变量

```python
>>> import os, sys
>>> 
>>> list(os.environ.keys())
['SHELL', 'SESSION_MANAGER', 'QT_ACCESSIBILITY', 'COLORTERM', 'XDG_CONFIG_DIRS', 'SSH_AGENT_LAUNCHER', 'XDG_MENU_PREFIX', 'GNOME_DESKTOP_SESSION_ID', 'GTK_IM_MODULE', 'CONDA_EXE', 'LANGUAGE', 'LC_ADDRESS', 'GNOME_SHELL_SESSION_MODE', 'LC_NAME', 'SSH_AUTH_SOCK', 'XMODIFIERS', 'DESKTOP_SESSION', 'LC_MONETARY', 'GTK_MODULES', 'PWD', 'LOGNAME', 'XDG_SESSION_DESKTOP', 'XDG_SESSION_TYPE', 'CONDA_PREFIX', 'XAUTHORITY', 'VIRTUALENVWRAPPER_VIRTUALENV', 'GJS_DEBUG_TOPICS', 'VIRTUALENVWRAPPER_SCRIPT', 'HOME', 'USERNAME', 'IM_CONFIG_PHASE', 'LC_PAPER', 'LANG', 'LS_COLORS', 'XDG_CURRENT_DESKTOP', 'VTE_VERSION', 'WAYLAND_DISPLAY', 'VIRTUALENVWRAPPER_WORKON_CD', 'CONDA_PROMPT_MODIFIER', 'GNOME_TERMINAL_SCREEN', 'VIRTUALENVWRAPPER_PYTHON', 'CLUTTER_IM_MODULE', 'GJS_DEBUG_OUTPUT', 'WORKON_HOME', 'GNOME_SETUP_DISPLAY', 'LESSCLOSE', 'XDG_SESSION_CLASS', 'TERM', 'LC_IDENTIFICATION', 'LESSOPEN', 'USER', 'GNOME_TERMINAL_SERVICE', 'CONDA_SHLVL', 'VIRTUALENVWRAPPER_PROJECT_FILENAME', 'DISPLAY', 'SHLVL', 'LC_TELEPHONE', 'QT_IM_MODULE', 'LC_MEASUREMENT', 'PAPERSIZE', 'CONDA_PYTHON_EXE', 'XDG_RUNTIME_DIR', 'CONDA_DEFAULT_ENV', 'LC_TIME', 'XDG_DATA_DIRS', 'PATH', 'VIRTUALENVWRAPPER_HOOK_DIR', 'GDMSESSION', 'DBUS_SESSION_BUS_ADDRESS', 'LC_NUMERIC', 'OLDPWD', '_']
>>> os.environ['PWD']
'/home/alone'
```

- 在`os.environ`中索引*shell*变量（如，`os.environ['PWD']`），类似*Unix shell*在变量名前添加一个`$`（比如，`$PWD`）



## 修改*shell*变量

```python
>>> os.environ['PWD'] = '/'
>>> os.environ['PWD']
'/'
```

- `os.environ`对象支持像普通字典一样的键索引以及赋值功能
- 在内部，对`os.environ`的键赋值将会调用`os.putenv`

示例：echo_env.py

```python
#!/usr/bin/env python
import os
from icecream import ic


ic('Hello,', os.environ['USER'])
```

- 无论以何种方式启动echo_env.py，总是显示运行它的*shell*的*USER*值

示例：set_env.py

```python
#!/usr/bin/env python
import os
from icecream import ic


ic('Hello', os.environ['USER'])

os.environ['USER'] = 'Tom'
os.system('./echo_env.py')

os.environ['USER'] = 'Peter'
print(os.popen('./echo_env.py').read())
```

- 脚本set_env.py简单地修改*shell*变量*USER*，然后派生另外一个脚本进程读取该变量值

输出：set_env.py

```python
beacherhou@alone-Vostro-14-5401:/media/beacherhou/Coding/Python/Python项目/pp4e/system$ ./set_env.py
ic| 'Hello', os.environ['USER']: 'beacherhou'
ic| 'Hello,', os.environ['USER']: 'Tom'
ic| 'Hello,', os.environ['USER']: 'Peter'
beacherhou@alone-Vostro-14-5401:/media/beacherhou/Coding/Python/Python项目/pp4e/system$ echo $USER
beacherhou
```

- 由此可见，**在最新版本的** ***Python*** **，赋给`os.environ`的键值将自动被导出到应用的其他部分。即赋值将同时改变** ***Python*** **程序中的`os.environ`对象，以及该进程对应的** ***shell*** **环境变量。** ***Python*** **程序、所有链入的** ***C*** **模块，所有该** ***Python*** **进程派生的子进程都可以看到新的赋值**
- **总而言之，一个子程序总是从它的父进程那里继承环境设置**
- 从更广泛的视角来看，像这样在启动程序前设置*shell*变量，是一种给程序传递信息的方式



## *shell*变量要点：父进程、`putenv`和`getenv`

- 注意之前示例的最后一行，在*Python*z的最顶层程序退出后，*USER*变量会变回初始值。赋给`os.environ`的键值被传到解释器的外部，然后**向下**传给子进程；然而它**永远不会向上**传递到父进程（包括*shell*）。在你的*Python*程序中对*shell*所做的设置**只对程序本身以及它所衍生的子程序有效**。
- 虽然对`os.environ`的修改会调用`os.putenv`，但**直接调用`os.putenv`却不会更新`os.environ`。**
- 如今，*Python*集中`os.getenv`调用，然而在大多数平台中，**它也只是简单地转换对`os.environ`的读取**。
