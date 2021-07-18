# 介绍`os`模块



## `os`模块中的工具

```python
>>> import os
>>> dir(os)
['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_TRAPPED', 'DirEntry', 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', 'F_LOCK', 'F_OK', 'F_TEST', 'F_TLOCK', 'F_ULOCK', 'MutableMapping', 'NGROUPS_MAX', 'O_ACCMODE', 'O_APPEND', 'O_ASYNC', 'O_CLOEXEC', 'O_CREAT', 'O_DIRECT', 'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_LARGEFILE', 'O_NDELAY', 'O_NOATIME', 'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 'O_RDONLY', 'O_RDWR', 'O_RSYNC', 'O_SYNC', 'O_TRUNC', 'O_WRONLY', 'POSIX_FADV_DONTNEED', 'POSIX_FADV_NOREUSE', 'POSIX_FADV_NORMAL', 'POSIX_FADV_RANDOM', 'POSIX_FADV_SEQUENTIAL', 'POSIX_FADV_WILLNEED', 'PRIO_PGRP', 'PRIO_PROCESS', 'PRIO_USER', 'P_ALL', 'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 'P_WAIT', 'PathLike', 'RTLD_DEEPBIND', 'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE', 'RTLD_NOLOAD', 'RTLD_NOW', 'R_OK', 'SCHED_BATCH', 'SCHED_FIFO', 'SCHED_IDLE', 'SCHED_OTHER', 'SCHED_RESET_ON_FORK', 'SCHED_RR', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'ST_APPEND', 'ST_MANDLOCK', 'ST_NOATIME', 'ST_NODEV', 'ST_NODIRATIME', 'ST_NOEXEC', 'ST_NOSUID', 'ST_RDONLY', 'ST_RELATIME', 'ST_SYNCHRONOUS', 'ST_WRITE', 'TMP_MAX', 'WCONTINUED', 'WCOREDUMP', 'WEXITED', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG', 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED', 'W_OK', 'XATTR_CREATE', 'XATTR_REPLACE', 'XATTR_SIZE_MAX', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit', '_fspath', '_fwalk', '_get_exports_list', '_putenv', '_spawnvef', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'chown', 'chroot', 'close', 'closerange', 'confstr', 'confstr_names', 'cpu_count', 'ctermid', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'environb', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir', 'fchmod', 'fchown', 'fdatasync', 'fdopen', 'fork', 'forkpty', 'fpathconf', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'fwalk', 'get_blocking', 'get_exec_path', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid', 'getgrouplist', 'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 'getpid', 'getppid', 'getpriority', 'getresgid', 'getresuid', 'getsid', 'getuid', 'getxattr', 'initgroups', 'isatty', 'kill', 'killpg', 'lchown', 'linesep', 'link', 'listdir', 'listxattr', 'lockf', 'lseek', 'lstat', 'major', 'makedev', 'makedirs', 'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty', 'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep', 'pipe', 'pipe2', 'popen', 'posix_fadvise', 'posix_fallocate', 'pread', 'preadv', 'putenv', 'pwrite', 'pwritev', 'read', 'readlink', 'readv', 'register_at_fork', 'remove', 'removedirs', 'removexattr', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sched_get_priority_max', 'sched_get_priority_min', 'sched_getaffinity', 'sched_getparam', 'sched_getscheduler', 'sched_param', 'sched_rr_get_interval', 'sched_setaffinity', 'sched_setparam', 'sched_setscheduler', 'sched_yield', 'sendfile', 'sep', 'set_blocking', 'set_inheritable', 'setegid', 'seteuid', 'setgid', 'setgroups', 'setpgid', 'setpgrp', 'setpriority', 'setregid', 'setresgid', 'setresuid', 'setreuid', 'setsid', 'setuid', 'setxattr', 'spawnl', 'spawnle', 'spawnlp', 'spawnlpe', 'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'st', 'stat', 'stat_result', 'statvfs', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sync', 'sys', 'sysconf', 'sysconf_names', 'system', 'tcgetpgrp', 'tcsetpgrp', 'terminal_size', 'times', 'times_result', 'truncate', 'ttyname', 'umask', 'uname', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitid', 'waitid_result', 'waitpid', 'walk', 'write', 'writev']
>>> dir(os.path)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_get_sep', '_joinrealpath', '_varprog', '_varprogb', 'abspath', 'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']
```

| 任务               | 工具                                                         |
| ------------------ | ------------------------------------------------------------ |
| Shell变量          | ```os.environ```                                             |
| 运行程序           | ```os.system```, ```os.popen```, ```os.execv```, ```os.spawnv```, ```os.execlp``` |
| 派生进程           | ```os.fork```, ```os.pipe```, ```os.waitpid```, ```os.kill``` |
| 文件描述符，文件锁 | ```os.open```, ```os.read```, ```os.write```                 |
| 文件处理           | ```os.remove```, ```os.rename```, ```os.mkfifo```, ```os.mkdir```, ```os.rmdir```, ```os.stat```, ```os.walk``` |
| 管理工具           | ```os.getcwd```, ```os.chdir```, ```os.chmod```, ```os.getpid```, `os.listdir`, `os.access` |
| 移植工具           | `os.sep`, `os.pathsep`, `os.curdir`, `os.path.split('path')`, `os.path.join`, `os.path.dirname('path')`, `os.path.basename('path')`, `os.path.splitext('path')`, `os.normpath('path')`, `os.abspath('path')` |
| 路径名工具         | `os.path.exists('path')`, `os.path.isdir('path')`, `os.path.isfile('path')`, `os.path.getsize('path')` |



## 管理工具

```python
>>> os.getpid()
4167
>>> os.getcwd()
'/home/alone'
>>> os.chdir('/')
>>> os.getcwd()
'/'
>>> os.chdir('/home/alone')
```

- `os.getpid()`: 返回调用函数的进程ID
- `os.getcwd()`: 返回当前的工作目录
- `os.chdir()`: 改变当前的工作目录



## 可移植的变量

```python
>>> os.pathsep, os.sep, os.pardir, os.curdir, os.linesep
(':', '/', '..', '.', '\n')
```

- `os.sep`: 目录组分隔符号
- `os.pathsep`: 在目录列表中分隔目录的字符
- `os.pardir`, `os.curdir`: 分别表示父级目录和当前目录
- `os.linesep`: 换行符



## 常见`os.path`工具

```python
>>> os.path.isdir('/home'), os.path.isfile('hello_world.py')
(True, True)
>>> os.path.exists('none.txt')
False
>>> os.path.getsize('/home/alone/hello_world.py')
23
>>> os.path.split('/home/alone/hello_world.py')
('/home/alone', 'hello_world.py')
>>> os.path.join('/home/alone', 'hello_world.py')
'/home/alone/hello_world.py'
>>> name = '/home/alone/hello_world.py'
>>> os.path.dirname(name), os.path.basename(name)
('/home/alone', 'hello_world.py')
>>> os.path.splitext(name)
('/home/alone/hello_world', '.py')
```

- ```os.path.isdir()```, ```os.path.isfile()```: 检查文件类型（若目录或文件不存在，则二者都返回False）
- ```os.exists()```: 测试文件是否存在
- ```os.getsize()```: 获取文件大小
- `os.path.split()`, `os.path.join()`: 一个将文件名从他的目录路径中剥离开来，另一个则将他们合并起来
- `os.path.dirname()`, `os.path.basename()`: 分别返回`os.path.split()`返回结果的前两项
- `os.path.splitext()`: 剥离了文件拓展名

```python
>>> os.sep
'/'
>>> os.path.split(name)
('/home/alone', 'hello_world.py')
>>> name.split(os.sep)													# 字符串方法
['', 'home', 'alone', 'hello_world.py']
>>> os.sep.join(name.split(os.sep))										# 字符串方法
'/home/alone/hello_world.py'
>>> os.path.join(*name.split(os.sep))
'home/alone/hello_world.py'
```

- 使用`str.split`和`str.join`几乎可起到与`os.sep`相同的作用

```python
>>> mixed = '/home//alone/./hello_world.py'
>>> os.path.normpath(mixed)
'/home/alone/hello_world.py'
>>> os.getcwd()
'/home/alone'
>>> os.path.abspath('')													# 空字符串代表当前目录
'/home/alone'
>>> os.path.abspath('文档/linux')										   # 扩展为当前工作目录下的路径
'/home/alone/文档/linux'
>>> os.path.abspath('.')												# 扩展相对路径
'/home/alone'
>>> os.path.abspath('..')
'/home'
>>> os.path.abspath('../../bin')
'/bin'
>>> os.path.abspath('/')												# 绝对路径不变
'/'
```

- `os.path.abspath()`: 可移植地返回文件的完整目录路径名



## 在脚本里运行shell命令

- `os.system()`: 在Python脚本中运行shell命令
- `os.popen()`: 运行shell命令并与其输入和输出流相连接

### 运行shell命令

```python
>>> os.system('cat hello_world.py')
print('Hello, world!')
0																		# 0只是系统调用自身的返回值
>>> os.system('cat helloworld.py')
cat: helloworld.py: 没有那个文件或目录
256																		# 通常用0表示成功
```

### 与shell命令进行通信

```python
>>> open('hello_world.py').read()
"print('Hello, world!')\n"
>>> text = os.popen('hello_world.py').read()
/bin/sh: 1: hello_world.py: not found
>>> text = os.popen('cat hello_world.py').read()
>>> text
"print('Hello, world!')\n"
>>> listing = os.popen('ls -alh').read
>>> listing = os.popen('ls -alh').readlines()
>>> listing
['总用量 130M\n', 'drwxr-xr-x 36 alone alone 4.0K  7月  5 14:19 .\n', 'drwxr-xr-x  3 root  root  4.0K  2月 19 19:01 ..\n', 'drwxr-xr-x  2 alone alone 4.0K  5月 16 19:19 公共的\n', 'drwxr-xr-x  2 alone alone 4.0K  2月 19 20:58 模板\n', 'drwxr-xr-x  2 alone alone 4.0K  6月  7 19:23 视频\n', 'drwxr-xr-x  2 alone alone 4.0K  7月  5 12:19 图片\n', 'drwxr-xr-x  4 alone alone 4.0K  7月  5 11:33 文档\n', 'drwxr-xr-x  3 alone alone 4.0K  7月  6 21:57 下载\n', 'drwxr-xr-x  2 alone alone 4.0K  5月 16 19:19 音乐\n', '-rw-rw-r--  1 alone alone  186  7月  5 14:19 优质壁纸图库，持续更新（有标签、大小、分辨率等，便于查找、管理）.txt\n', 'drwxr-xr-x  2 alone alone 4.0K  7月  6 22:46 桌面\n', 'drwxrwxr-x  3 alone alone 4.0K  5月  2 22:05 adobe_flash_player\n', 'drwxrwxr-x  3 alone alone 4.0K  2月 20 15:01 .anaconda\n', 'drwxrwxr-x 23 alone alone 4.0K  2月 20 14:58 anaconda3\n', 'drwxrwxr-x  8 alone alone 4.0K  3月 26 15:29 .atom\n', '-rw-------  1 alone alone  11K  7月  8 16:48 .bash_history\n', '-rw-r--r--  1 alone alone  220  2月 19 19:01 .bash_logout\n', '-rw-r--r--  1 alone alone 4.5K  2月 20 20:31 .bashrc\n', '-rw-r--r--  1 alone alone 3.8K  2月 20 14:58 .bashrc-anaconda3.bak\n', 'drwx------  2 alone alone 4.0K  7月  2 19:29 .bypy\n', 'drwxrwxr-x 31 alone alone 4.0K  6月  7 17:49 .cache\n', 'drwxrwxr-x  3 alone alone 4.0K  2月 20 20:43 .conda\n', '-rw-rw-r--  1 alone alone   40  2月 20 15:02 .condarc\n', 'drwx------ 29 alone alone 4.0K  7月  8 16:45 .config\n', 'drwxrwxr-x  2 alone alone 4.0K  7月  2 19:26 cron_job\n', '-rwxrwxrwx  1 alone alone 2.1K  7月  4 21:27 download.py\n', 'drwx------  2 alone alone 4.0K  6月 30 22:33 .gconf\n', 'drwx------  3 alone alone 4.0K  7月  7 20:46 .gnupg\n', '-rw-rw-r--  1 alone alone   23  5月 16 21:17 hello_world.py\n', 'drwxr-xr-x  5 alone alone 4.0K  6月  5 21:57 .ipython\n', 'drwxrwxr-x  3 alone alone 4.0K  6月  8 16:50 Library\n', 'drwxr-xr-x  5 alone alone 4.0K  2月 19 21:08 .local\n', 'drwx------  5 alone alone 4.0K  2月 19 19:08 .mozilla\n', '-rwxrwxrwx  3 alone alone  86M  5月 21 19:49 Obsidian-0.12.3.AppImage\n', '-rw-r--r--  1 alone alone  363  5月 16 19:19 .pam_environment\n', '-rwxrwxrwx  1 alone alone  43M  4月 17 11:38 panda5.1.0-x86_64.appimage\n', 'drwxrwxr-x  2 alone alone 4.0K  2月 19 19:07 .pandaconfig\n', 'drwxrwxr-x  2 alone alone 4.0K  2月 20 14:39 .pip\n', 'drwx------  3 alone alone 4.0K  2月 19 19:15 .pki\n', '-rw-r--r--  1 alone alone  807  2月 19 19:01 .profile\n', '-rw-------  1 alone alone    7  2月 20 20:35 .python_history\n', 'drwxr-xr-x  5 alone alone 4.0K  6月 19 21:51 snap\n', '-rw-rw-r--  1 alone alone   21  6月 20 22:28 spam.txt\n', 'drwx------  2 alone alone 4.0K  4月 18 11:46 .ssh\n', 'drwxrwxr-x  5 alone alone 4.0K  6月  7 19:19 .ssr\n', '-rw-r--r--  1 alone alone    0  2月 19 20:54 .sudo_as_admin_successful\n', 'drwxrwxr-x  2 alone alone 4.0K  7月  5 11:21 temporary data\n', '-rw-------  1 alone alone 236K  5月 21 22:20 .test.html.swp\n', 'lrwxrwxrwx  1 alone alone   13  7月  5 11:33 USB -> /media/alone/\n', 'drwxr-xr-x  2 alone alone 4.0K  5月  4 22:20 .vim\n', '-rw-------  1 alone alone  16K  7月  5 13:15 .viminfo\n', '-rw-rw-r--  1 alone alone  141  2月 19 21:17 .vimrc\n', 'drwxrwxr-x  3 alone alone 4.0K  2月 20 14:47 .virtualenvs\n', 'drwxrwxr-x  3 alone alone 4.0K  7月  3 21:28 .vscode\n', '-rw-rw-r--  1 alone alone 2.3K  7月  4 21:34 wallhaven_download.py\n', 'drwxr-xr-x  5 alone alone 4.0K  4月 15 12:00 wordpress\n']
>>> os.system('python hello_world.py')
Hello, world!
0
>>> output = os.popen('python hello_world.py').read()
>>> output
'Hello, world!\n'
```

### 替代方案：`subprocess`模块

```python
>>> import subprocess
>>> subprocess.call('python hello_world.py', shell=True)									# 类似os.system()
Hello, world!																				# shell=True: 内建shell命令
0
```

- 这是模拟`os.system()`
- 更深入的讨论我们放在后面。现在只需要记住在类Unix环境下运行时，如果**依赖程序路径查找等shell功能**，那么可能传入`shell=Ture`就行了

```python
>>> pipe = subprocess.Popen('python hello_world.py', shell=True, stdout = subprocess.PIPE)
>>> pipe.communicate()
(b'Hello, world!\n', None)
>>> pipe.returncode
0
```

- 这是模拟`os.popen()`
- 我们将`stdout`流与管道连接，然后用`communicate()`来运行命令，并接受它的标准输出流和错误流文本；运行完成后，命令的退出状态可作为属性来查看

```python
>>> pipe = subprocess.Popen('python hello_world.py', shell=True, stdout=subprocess.PIPE)
>>> pipe.stdout.read()
b'Hello, world!\n'
>>> pipe.wait()
0
```

- 我们还可以用其他接口直接读取命令的标准输出流，然后等待命令退出（并返回退出状态）

```python
>>> from subprocess import Popen, PIPE
>>> Popen('python hello_world.py', shell=True, stdout=PIPE).communicate()[0]
b'Hello, world!\n'
>>> 
>>> import os
>>> os.popen('python hello_world.py').read()
'Hello, world!\n'
```

- 实际上，`os.popen()`和`subprocess.Popen`存在着直接的映射关系

### shell命令的局限

#### `os.system()`和`os.popen()`的两大局限

1. 可移植程度取决于所运行的命令
2. 它们通常在新进程里执行这些命令，会大幅降低程序运行速度

#### 阻塞程序

- `os.system()`通常会、阻塞程序，直到所启动的命令行程序退出，只需在命令行代码末尾加上shell后台运算符`&`即可
- 新近的Python版本加入了`os.startfile()`，它会打开一个文件，无论文件的类型是什么，就像用鼠标单击它一样（在相应的应用程序内打开文件）
- `os.popen()`一般不会阻塞，但在管道对象在所启动的程序退出前关闭（如进行垃圾回收时），或是管道一次性完成读取（如用`read()`），那么仍然有可能阻塞



## `os`模块导出的其他工具

- `os.environ`: 获取和设置shell环境变量
- `os.fork`: 在类Unix系统下派生新的子进程
- `os.pipe`: 负责程序间通信
- `os.execlp`: 启动新程序
- `os.spawnv`: 启动带有底层控制的新程序
- `os.open`: 打开基于底层描述符的文件
- `os.mkdir`: 创建新目录
- `os.mkfifo`: 创建新的命名管道
- `os.stat`: 获取文件底层信息
- `os.remove`: 根据路径名删除文件
- `os.walk`: 将函数或循环应用于整个目录树的各部分
