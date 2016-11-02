# coding=utf-8
# 如何判断字符串a是否以字符串b开头或结尾
# 使用字符串的str.startswith(),str.endswith()方法，多个匹配时参数使用元组
# endswith()接受一个元组作为参数
import os, stat

os.listdir('.')#显示当前目录下文件
s = 'g.sh'
s.endswith('.sh')#返回True
s.endswith(('.sh', '.py'))#返回也是true
[for name in os.listdir('.') if name.endswith(('.sh', '.py'))]

os.stat('e.py').st_mode #访问e.py权限，返回十进制数
oct(os.stat('e.py').st_mode)
stat.S_IXUSR#此权限是可执行权限
os.chmod('e.py', os.stat('e.py').st_mode | stat.S_IXUSR)#更改权限为用户可执行
