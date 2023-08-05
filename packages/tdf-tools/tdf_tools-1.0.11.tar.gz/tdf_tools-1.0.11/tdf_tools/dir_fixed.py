#!/usr/bin/env python
# encoding=utf-8

import os

from tdf_tools.tdf_print import printDebug

genDirName = '.tdf_flutter'

# 向上遍历寻找.tdf_flutter存在的目录，找到则


def goSearchDir(level):
    os.chdir(os.path.abspath(r".."))
    curDir = os.getcwd()
    for root, dirs, files in os.walk(curDir):
        if str(genDirName) in dirs:
            return
    ex = Exception('未发现.tdf_flutter目录')
    raise ex

    # if level > 1:
    #     ex = Exception('未发现.tdf_flutter目录')
    #     # 抛出异常对象
    #     raise ex

    # curDir = os.getcwd()
    # for root, dirs, files in os.walk(curDir):
    #     print(level)
    #     if str(genDirName) in dirs:
    #         print(os.getcwd())
    #     else:
    #         os.chdir(os.path.abspath(r".."))
    #         goSearchDir(level + 1)


global curDir
curDir = os.getcwd()


def goInShellDir():
    os.chdir(curDir)
    # os.chdir(os.path.abspath(os.path.dirname(__file__)))
    # printDebug(os.getcwd())

# 进入.tdf_flutter文件夹


def goInTdfFlutterDir():
    goInShellDir()
    if os.path.exists('pubspec.yaml'):
        try:
            goSearchDir(0)
        except:
            goInShellDir()
            os.chdir(os.path.abspath(r".."))
            os.mkdir('.tdf_flutter')
    os.chdir('.tdf_flutter')


# 进入缓存文件目录


def goTdfCacheDir():
    goInShellDir()
    if os.path.exists('tdf_cache'):
        os.chdir('tdf_cache')
    elif os.path.exists('tdf_cache') is not True:
        create = input('当前目录没有找到.tdf_cache缓存文件夹，是否创建？(y/n):')
        if create == 'y':
            os.mkdir('tdf_cache')
        else:
            print('Oh,it\'s disappointing.')
            exit(1)
