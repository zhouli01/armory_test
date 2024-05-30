# -*- coding: utf-8 -*-
import shutil
import subprocess
import sys
import logging
import time
import pyautogui
import platform

def armory_linux_cmd1():
    pass

def armory_win_cmd1():
    pass


def armory_help():
    # 查看armory命令帮助
    armory1 = subprocess.getoutput("armory")
    logging.info('armory 查看帮助：%s', armory1)

    armory_h = subprocess.getoutput("armory -h")
    logging.info('armory -h 查看帮助：%s', armory_h)

    armory__help = subprocess.getoutput("armory --help")
    logging.info('armory --help 查看帮助：%s', armory__help)

    armory_help1 = subprocess.getoutput("armory help")
    logging.info('armory help 查看帮助：%s', armory_help1)

def armory_v():
    # 查看armory版本号
    armory_v1 = subprocess.getoutput("armory -v")
    logging.info('armory -v 查看版本号：%s', armory_v1)

    armory__version = subprocess.getoutput("armory --version")
    logging.info('armory --version 查看版本号：%s', armory__version)


def armory_init():
    # 执行armory init命令，初始化软件包666
    armory_init_666 = subprocess.getoutput("armory init 666")
    logging.info('armory init 666 执行结果：%s', armory_init_666)

    #本地删除目录666
    logging.info("666 创建成功")
    shutil.rmtree('./666')
    logging.info("666 删除成功")

    # 执行armory init命令，初始化软件包@test/666
    armory_init_test = subprocess.getoutput("armory init @test/666")
    logging.info('armory init @test/666 执行结果：%s', armory_init_test)

    #本地删除目录@test
    logging.info("@test 创建成功")
    shutil.rmtree('./@test')
    logging.info("@test 删除成功")


def armory_repo_ls_bak():
    # armory 的repo 管理
    subprocess.call("armory repo ls")
    time.sleep(3)
    im = pyautogui.screenshot('./Picture/armory_repo_ls.png', region=(0, 800, 900, 500))
    logging.info('armory repo ls 执行结果见Picture目录下对应文件名截图')



def armory_repo_ls_win():
    # armory的repo管理
    res = subprocess.check_output("armory repo ls")
    armory_repo=res.decode('utf-8')
    logging.info('armory repo ls 执行结果：%s', armory_repo)

#需要继续调试
def armory_repo_ls_linux():
    # armory的repo管理
    armory_repo_ls=subprocess.getoutput("armory repo ls")
    #print("armory_repo_ls:",armory_repo_ls)
    logging.info('armory repo ls 执行结果：%s', armory_repo_ls)

def armory_repo_use():
    #切换当前使用的repo
    armory_repo_use_QA = subprocess.getoutput("armory repo use QA")
    logging.info('armory repo use 执行结果：%s', armory_repo_use_QA)

def armory_login():
    # armory login登录
    armory_login_zhouli = subprocess.getoutput("armory login  -u zhouli -p 111111")
    logging.info('armory login 执行结果：%s', armory_login_zhouli)

def armory_whoami():
    # armory whoami 查看当前登录用户
    whoami = subprocess.getoutput("armory whoami")
    logging.info('armory whoami 执行结果：%s', whoami)


def armory_config():
    # armory config ls  查看armory的配置
    armory_config_ls = subprocess.getoutput("armory config ls")
    logging.info('armory config ls 执行结果：%s', armory_config_ls)

    # 关闭进度条
    armory_config_set = subprocess.getoutput("armory config set disableProgressBar=true")
    logging.info('armory config set 执行结果：%s', armory_config_set)

    #config修改后,查看armory的配置
    armory_config_set_ls = subprocess.getoutput("armory config ls")
    logging.info('armory config set 后查看config：%s', armory_config_set_ls)

def armory_version():
    # armory version 版本管理
    armory_version_h = subprocess.getoutput("armory version -h")
    logging.info('armory version -h 执行结果：%s', armory_version_h)

    # armory版本升级
    armory_version_update = subprocess.getoutput("armory version update 1.5.2")
    logging.info('armory version update 执行结果：%s', armory_version_update)

def armory_publish():
    # armory发布软件包
    armory_publish_1408 = subprocess.getoutput("armory publish")
    logging.info('armory publish 执行结果：%s', armory_publish_1408)

def armory_get():
    # armory下载软件包
    armory_get_1408 = subprocess.getoutput("armory get @0401/1408@0.0.1")
    logging.info('armory get 执行结果：%s', armory_get_1408)

    #本地删除下载的软件包
    shutil.rmtree('./@0401')
    logging.info("@0401 删除成功")

def armory_search_bak():
    # armory search 搜索软件包  暂时有点兼容性问题
    subprocess.call("armory search @armory/armory-cli")
    time.sleep(3)
    im = pyautogui.screenshot('./Picture/armory_search.png', region=(0, 800, 1300, 500))
    logging.info('armory search @armory/armory-cli 执行结果见Picture目录下对应文件名截图')

def armory_search_win():
    # armory search 搜索软件包,插件并不能完全支持，待改进
    armory_search_armory_cli=subprocess.getoutput("armory search @armory/armory-cli")
    logging.info('armory search 执行结果：%s', armory_search_armory_cli)

def armory_search_linux():
    # armory search 搜索软件包,插件并不能完全支持，待改进
    armory_search_armory_cli=subprocess.getoutput("armory search @armory/armory-cli")
    #print("armory_search_armory_cli:",armory_search_armory_cli)
    logging.info('armory search 执行结果：%s', armory_search_armory_cli)

def armory_dep():
    # armory dep 帮助信息
    armory_dep_h = subprocess.getoutput("armory dep -h")
    logging.info('armory dep -h 执行结果：%s', armory_dep_h)

    # armory dep 查看软件包依赖
    armory_dep_ls = subprocess.getoutput("armory dep ls bbb@0.0.1")
    logging.info('armory dep ls 执行结果：%s', armory_dep_ls)

def armory_tag_h():
    # armory tag 帮助信息
    armory_tag = subprocess.getoutput("armory tag -h")
    logging.info('armory tag -h 执行结果：%s', armory_tag)

def armory_tag_ls_bak():
    # armory tag 查看软件包tag
    subprocess.call("armory tag ls  @armory/armory-cli")
    time.sleep(3)
    im = pyautogui.screenshot('./Picture/armory_tag_ls.png', region=(0, 800, 1300, 600))
    logging.info('armory tag ls  @armory/armory-cli 执行结果见Picture目录下对应文件名截图')


def armory_tag_ls_win():
    # armory tag 帮助信息
    res= subprocess.check_output("armory tag ls  @armory/armory-cli")
    armory_tag_ls=res.decode('utf-8')
    logging.info('armory tag ls  @armory/armory-cli 执行结果：%s', armory_tag_ls)

def armory_tag_ls_linux():
    # armory tag 查看软件包tag
    armory_tag_ls=subprocess.getoutput("armory tag ls  @armory/armory-cli")
    #print("armory_tag_ls:",armory_tag_ls)
    logging.info('armory  tag ls 执行结果：%s', armory_tag_ls)

def armory_logout():
    # armory logout 退出登录
    armory_logout1 = subprocess.getoutput("armory logout")
    logging.info('armory logout 执行结果：%s', armory_logout1)

def armory_step1():
    armory_help()
    armory_v()
    armory_init()


def armory_step2():
    armory_repo_use()
    armory_login()
    armory_whoami()
    armory_config()
    armory_version()
    armory_publish()
    armory_get()

def armory_step3():
    armory_dep()
    armory_tag_h()

def armory_step4():
    armory_logout()

def armory_win_cmd():
    print("cmd 在 windows 测试开始")
    logging.info("cmd 在 windows 测试开始")
    # 执行 armory命令
    armory_step1()
    armory_repo_ls_win()
    armory_step2()
    armory_search_win()
    armory_step3()
    armory_tag_ls_win()
    armory_step4()
    logging.info('-------------------本次 win 测试完成-------------------')

def armory_linux_cmd():
    print("cmd 在 linux 测试开始")
    logging.info("cmd 在 linux 测试开始")
    armory_step1()
    armory_repo_ls_linux()
    armory_step2()
    armory_search_linux()
    armory_step3()
    armory_tag_ls_linux()
    armory_step4()
    logging.info('-------------------本次 linux 系统测试完成-------------------')

def armory_win():
    print("在 windows 测试开始")
    logging.info("在 windows 测试开始")
    armory_win_cmd()

def armory_linux():
    print("在 linux 测试开始")
    logging.info("在 linux 测试开始")
    armory_linux_cmd()


def system_os_bak():
    if sys.platform.startswith('win'):
        print("当前是: Windows 操作系统")
        logging.info("当前是: Windows 操作系统")
        armory_win()

    elif sys.platform.startswith('linux'):
        print("当前是: Linux操作系统")
        logging.info("当前是: Linux操作系统")
        armory_linux()
    elif sys.platform.startswith('darwin'):
        print("当前是: macOS操作系统")
    else:
        print("当前是: 其他操作系统")


def system_os():
    if platform.system() == 'Windows':
        print("当前是: Windows 操作系统")
        logging.info("当前是: Windows 操作系统")
        armory_win()

    elif platform.system() =='Linux':
        print("当前是: Linux操作系统")
        logging.info("当前是: Linux操作系统")
        armory_linux()

    elif platform.system() =='Macos':
        print("当前是: macOS操作系统")
    else:
        print("当前是: 其他操作系统")


if __name__ == '__main__':

    os=platform.system()
    timestamp = int(time.time())
    #日志命名格式
    logging.basicConfig(filename='./LOG/' + 'armory-'+ os +'-'+ str(timestamp) + '.log', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',encoding='utf-8')

    #判断当前系统，执行不同的方法体
    system_os()





