https://www.runoob.com/python3/python3-type-conversion.html

command:
    python --version

main:
    if __name__ == '__main__':

语法:
    没有;
    一般用:和缩进控制语句块
    空方法: 用 pass
获取参数:
    import sys

    # 获取脚本名称
    script_name = sys.argv[0]

    # 获取命令行参数
    arguments = sys.argv[1:]

规范:
    文件,小写+下划线
    类名: 大写开头, 驼峰 class DefineClz:
          构造器: def __init__(self):
          类变量   需要声明
          实例变量 需要声明
          类方法
          实例方法
          静态方法
          继承:
            class SonClz(ParrentClz):
        

    变量命名:  全小写, 下划线分割
               不能命名和关键字和数据类型相同, 例如 不能变量命名为str, 因为str是string字符串的数据类型.同时也有str()方法

flow:
    with xx as xxx:
        #作用: 可以自动回收资源,会先调用xx类的__enter__()方法,结束时候xx类里面实现__exit___()方法.
        #此外: python还有其他协商好的双下划线方法,也叫魔术方法, __str__

模块引入:
    import sys
    import os
    import numpy as np
    from my_module import my_function

框架:
    flask:  轻量web
    Django: 全能web
        1.概述框架:
            是一个用模板文件(渲染到前端html,类似Thymeleaf,freemarker),集成数据库等的一个web框架
            需要pip先安装下载Django, 里面就是整理好的一个项目,带有管理后台和db init sql等,可以和sqllite集成.
            启动: python manage.py runserver 0.0.0.0:8080
            配置都在settings.py里面,包括配置client可访问域范围
            

        2.额外说明:
            虚拟环境: virtualenv
                pip install virtualenv
                pip install virtualenvwrapper
                    #好像还需要配置环境变量WORKON_HOME,
                    https://blog.51cto.com/u_14125/6496612
                作用:
                    依赖隔离： 每个虚拟环境都拥有独立的 Python 解释器和包管理系统，可以确保不同项目之间的依赖关系不冲突
                        方便每个项目都用不同版本的依赖.
                    版本管理： 可以在不同的虚拟环境中使用不同的 Python 版本，并根据需要管理项目所需的不同 Python 包的版本。
                    整洁性和维护性： 通过使用虚拟环境，可以使项目更整洁，并简化依赖项管理。
                概述:会在一个virtualenv配置文件目录下创建一个虚拟环境的目录作为当前项目运行的环境.达到隔离的目的.
                使用:
                    mkvirtualenv testenv -p python3/python3安装路径
                    workon testenv #切换虚拟环境
            自定义二方包lib
                disutil打包工具,有点像maven
                通过使用distutils提供的命令，我们可以将Python项目打包为tar、zip等格式，方便分发。
                使用:
                    1.配置setup.py, 配置依赖名称,作者等信息
                    2.python setup.py sdist bdist_wheel
                        pip install .
        3.打包部署
            依赖处理:
                pip freeze > requirements.txt  #这个文件放到服务器,服务器可以依据这份文件下载依赖
            部署可以用gunicorn或者wsgi
            gunicorn
                作用: 用于部署项目 ,是一个wsgi http服务器
                pip install gunicorn
                gunicorn -h
                部署:
                #准备配置文件gunicorn_config.py, 里面可以配置项目端口,日志,线程数,python路径,环境变量等
                方式1:
                    gunicorn -c gunicorn_config.py  #默认用当前目录作用运行目录,即需要在项目工作目录下运行命令,或者设置配置working directory
                方式2:
                #w表示线程, main表示main.py, app表示实例化当前程序名为app
                gunicorn -w 4 -b 0.0.0.0:8080 main:app
                #异步模式-k gevent 需要先pip下载gevent
                
            wsgi:
                Django内置wsgi web server gateway interface 协议
                pip3 install uwsgi
                如何部署: 配置好wsgi.ini文件,用命令启动即可
                    [uwsgi]
                    chdir=/path/to/your/project
                    module=mysite.wsgi:application
                    master=True
                    pidfile=/tmp/project-master.pid
                    vacuum=True
                    max-requests=5000
                    daemonize=/var/log/uwsgi/yourproject.log
                uwsgi --ini uwsgi.init
                

            4.总结部署思路:
                1.git commit/push项目之后
                2.pipeline tar 打包项目
                3.服务器拿到项目解压
                4.准备环境, 比如虚拟环境准备, pip 安装包准备, 替换相关配置文件,比如server host等
                5.使用wsgi/gunicore 启动项目
                6.如果使用容器化部署, 可以不比准虚拟环境, 镜像里面包含python和pip命令即可.
                缺陷: 需要动态下载包, pip install 包不稳定, 包变更了或者下载失败
            5.打包发布:
                pyinstaller
                    pyi-makespec -D manage.pyi  #项目目录生成manager.spec
                    pyinstall manager.spec      #打包: 生成build和dist目录
                        需要一些配置修改,然后运行manager.exe

        Docker部署方式:
            1.image:
                需要RUN pip install包, 在package image的时候就准备好依赖.

            

    Pyramid:通用web

pip安装使用其他原
    -i https://pypi.tuna.tsinghua.edu.cn/simple

