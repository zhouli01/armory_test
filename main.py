# -*- coding: utf-8 -*-

import shutil
import subprocess
import sys
import logging
import time
import pyautogui

def armory_win_cmd1():
    pass


def armory_win_cmd():
    print("cmd 在windows 测试开始")
    # 执行 armory命令
    armory1 = subprocess.getoutput("armory")
    logging.info('armory 查看帮助：%s', armory1)

    # 查看armory版本号
    armory2 = subprocess.getoutput("armory -v")
    logging.info('armory -v 查看版本号：%s', armory2)

    armory3 = subprocess.getoutput("armory --version")
    logging.info('armory --version 查看版本号：%s', armory3)

    # 查看armory命令帮助
    armory_h = subprocess.getoutput("armory -h")
    logging.info('armory -h 查看帮助：%s', armory_h)

    armory__help = subprocess.getoutput("armory --help")
    logging.info('armory --help 查看帮助：%s', armory__help)

    armory_help = subprocess.getoutput("armory help")
    logging.info('armory help 查看帮助：%s', armory_help)

    # 执行armory init命令，初始化软件包
    armory_init = subprocess.getoutput("armory init 666")
    logging.info('armory init 666 执行结果：%s', armory_init)
    logging.info("666 创建成功")
    shutil.rmtree('./666')
    logging.info("666 删除成功")

    armory_init1 = subprocess.getoutput("armory init @test/666")
    logging.info('armory init @test/666 执行结果：%s', armory_init1)
    logging.info("@test 创建成功")
    shutil.rmtree('./@test')
    logging.info("@test 删除成功")

    # armory 的repo 管理
    subprocess.call("armory repo ls")
    time.sleep(3)
    im = pyautogui.screenshot('./Picture/armory_repo_ls.png', region=(0, 800, 900, 500))
    logging.info('armory repo ls 执行结果见Picture目录下对应文件名截图')

    armory_repo_use = subprocess.getoutput("armory repo use QA")
    logging.info('armory repo use 执行结果：%s', armory_repo_use)

    # armory login登录
    armory_login = subprocess.getoutput("armory login -u zhouli -p 111111")
    logging.info('armory login 执行结果：%s', armory_login)

    # armory whoami 查看当前登录用户
    armory_whoami = subprocess.getoutput("armory whoami")
    logging.info('armory whoami 执行结果：%s', armory_whoami)

    # armory config ls  查看armory的相关配置
    armory_config_ls = subprocess.getoutput("armory config ls")
    logging.info('armory config ls 执行结果：%s', armory_config_ls)

    # armory version 版本管理
    armory_version_h = subprocess.getoutput("armory version -h")
    logging.info('armory version -h 执行结果：%s', armory_version_h)

    # armory版本升级
    armory_version_update = subprocess.getoutput("armory version update 1.5.2")
    logging.info('armory version update 执行结果：%s', armory_version_update)

    # 关闭进度条
    armory_config_set = subprocess.getoutput("armory config set disableProgressBar=true")
    logging.info('armory config set 执行结果：%s', armory_config_set)

    # armory发布软件包
    armory_publish = subprocess.getoutput("armory publish")
    logging.info('armory publish 执行结果：%s', armory_publish)

    # armory下载软件包
    armory_get = subprocess.getoutput("armory get @0401/1408@0.0.1")
    logging.info('armory get 执行结果：%s', armory_get)
    shutil.rmtree('./@0401')
    logging.info("@0401 删除成功")

    # armory search 搜索软件包  暂时有点兼容性问题
    subprocess.call("armory search @armory/armory-cli")
    time.sleep(3)
    im = pyautogui.screenshot('./Picture/armory_search.png', region=(0, 800, 1300, 500))
    logging.info('armory search @armory/armory-cli 执行结果见Picture目录下对应文件名截图')

    # armory dep 帮助信息
    armory_dep_h = subprocess.getoutput("armory dep -h")
    logging.info('armory dep -h 执行结果：%s', armory_dep_h)
    # armory dep 查看软件包依赖
    armory_dep_ls = subprocess.getoutput("armory dep ls bbb@0.0.1")
    logging.info('armory dep ls 执行结果：%s', armory_dep_ls)

    # armory tag 帮助信息
    armory_tag_h = subprocess.getoutput("armory tag -h")
    logging.info('armory tag -h 执行结果：%s', armory_tag_h)

    # armory tag 查看软件包tag
    subprocess.call("armory tag ls  @armory/armory-cli")
    time.sleep(3)
    im = pyautogui.screenshot('./Picture/armory_tag_ls.png', region=(0, 800, 900, 500))
    logging.info('armory tag ls  @armory/armory-cli 执行结果见Picture目录下对应文件名截图')

    # armory logout 退出登录
    armory_logout = subprocess.getoutput("armory logout")
    logging.info('armory tag ls 执行结果：%s', armory_logout)
    logging.info('-------------------本次测试完成-------------------')


def armory_win_powershell():
    print("powershell 在windows 测试开始")


def armory_win_gitbash():
    print("gitbash 在windows 测试开始")


def armory_win():
    print("在windows 测试开始")

    armory_win_cmd()
    # armory_win_powershell()
    # armory_win_gitbash()


if __name__ == '__main__':
    timestamp = int(time.time())
    logging.basicConfig(filename='./LOG/' + 'armory-' + str(timestamp) + '.log', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')

    if sys.platform.startswith('win'):
        # print("当前是: Windows 操作系统")
        armory_win()

    elif sys.platform.startswith('linux'):
        print("Linux操作系统")
    elif sys.platform.startswith('darwin'):
        print("macOS操作系统")
    else:
        print("其他操作系统")
