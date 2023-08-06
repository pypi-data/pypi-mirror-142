#!/usr/bin/env python
# 通过 setuptools 模块导入所需要的函数
from distutils.core import setup
from setuptools import find_packages

setup(name='stephyoung',
      version='1.0',
      #description='Python Distribution Utilities',
      author='Yangbin',
      #author_email='gward@python.net',
      #url="ckh.handsome.com", 此网站需要存在且未被占用
      #url='https://www.python.org/sigs/distutils-sig/',
      packages = find_packages("stephyoung"),
      package_dir= {"":"stephyoung"},
      package_data= {
          "":[".txt",".info","*.properties",".py"],
          "":["data/*.*"],
      },
      #packages=['distutils', 'distutils.command'],
# 取消所有测试包
    exclude = ["*.test","*.test>","test.*","test"]
)
