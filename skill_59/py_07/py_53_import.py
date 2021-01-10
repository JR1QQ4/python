#!/usr/bin/python
# -*- coding:utf-8 -*-
# 第 53 条: 用虚拟环境隔离项目，并重建其依赖关系

# 借助虚拟环境，我们可以在同一台电脑上同时安装某软件包的多个版本，而且能保证它们不会冲突
# pyvenv 命令可以创建虚拟环境，source bin/activate 命令可以激活虚拟环境，deactivate 命令可以停用虚拟环境
# pip freeze 命令可以把某套环境所依赖的软件包，汇总到一份文件里面。我们把这个 requirement.txt 文件提供给 pip install -r 命令，
#   即可重建一套与原环境相仿的新环境
# 如果使用 Python 3.4 之前的版本做开发，那么必须单独下载并安装类似的 pyvenv 工具。那个命令行工具不叫 pyvenv，而是叫做 virtualenv









