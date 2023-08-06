#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:renameFiles.py
# author:PigKnight
# datetime:2022/3/6 16:57
# software: PyCharm
"""
this is function description
"""
# import module your need
import os
import sys
import click

from .commons import info_dir


# 文件批量重命名
@click.command()
@click.option('--path', '-p', required=False, type=str, help='Path to the file to process')
@click.option('--order', '-o', required=False, type=click.Choice(['name', 'path', 'size']), help='Used for order')
@click.option('--order_rule', '-or', required=False, default='desc', type=click.Choice(['desc', 'asc']),
              help='order with desc/asc')
@click.option('--pre', required=False, type=str, help='Used for file renaming as a prefix')
@click.option('--name', required=False, type=str, help='Used for file renaming as a filename')
@click.option('--suf', required=False, type=str, help='Used for file renaming as a suffix')
def rename_files(**kwargs):
    # 参数接收
    path = kwargs.get('path') or '.'
    order = kwargs.get('order') or 'size'
    pre = kwargs.get('pre') or ''
    name = kwargs.get('name')
    suf = kwargs.get('suf') or ''

    # 确认工作目录
    os.chdir(path)

    # 获取工作目录文件信息
    file_list_ordered = info_dir(path=path, order=order)

    flag = input("将要处理的目录为:{0}，共{1}个文件，是否确认(Y/N)".format(os.getcwd(), len(file_list_ordered)))
    if flag.upper() != 'Y':
        print("任务已取消！")
        sys.exit()

    # 批量重命名
    os.chdir(path)
    total_files = len(file_list_ordered)
    for index in range(1, total_files + 1):
        file = file_list_ordered[index - 1]
        old_filename = file['shortname'] + file['extension']
        if name:
            new_filename = '{0}{1}{2}{3}{4}'.format(pre, name, suf, str(index), file['extension'])
        else:
            new_filename = '{0}{1}{2}{3}{4}'.format(pre, file['shortname'], suf, str(index), file['extension'])
            print(new_filename)
        try:
            os.rename(old_filename, new_filename)
            print("{0} 已被重命名为 {1}，当前进度：{2}/{3}".format(old_filename, new_filename, index, total_files))
        except Exception as e:
            print("{0} 重命名失败!当前进度：{1}/{2}，错误原因：{3}".format(old_filename, index, total_files, e))

    print('文件已重命名完成!')


if __name__ == '__main__':
    rename_files()
