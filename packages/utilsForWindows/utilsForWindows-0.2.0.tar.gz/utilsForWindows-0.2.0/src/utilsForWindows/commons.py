#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:commons.py
# author:BlueLvRen
# datetime:2022/3/11 0:29
# software: PyCharm
"""
this is function description
"""
# import module your need
# from commons import info_list
import os
import sys

# 查看目录信息
import click


def info_dir(path='.', order='size'):
    if not os.path.isdir(path):
        print('请输入正确的文件夹路径')
        sys.exit()
    filename_list = os.listdir(path)
    dict_list = []

    if order not in ['name', 'path', 'size']:
        order = 'size'

    # 获得排序后的字典列表
    for filename in filename_list:
        filepath = os.path.join(path, filename)
        shortname, extension = os.path.splitext(filename)
        if os.path.isfile(filepath):
            file_info = {'shortname': shortname, 'extension': extension, 'path': filepath,
                         'size': os.path.getsize(filepath)}
            dict_list.append(file_info)

    file_list_ordered = sorted(dict_list, key=lambda keys: keys.get(order))

    return file_list_ordered


# 查看所有功能
def info_function():
    print("输入 '<command> --help' 以获取功能的选项与参数")
    print("u_ren/u_rename 批量重命名文件")
