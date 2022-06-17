# XunDog
个人博客搭建
开发环境: Pycharm、Debian、Python3.7、Django2.2、虚拟环境venv、Mysql
功能模块：实现了博文管理、用户管理、多级评论、文章栏目和标签、图片处理、第三方登录、点赞、搜索、最新/热度排序。


依赖库安装
pip install -U pip
pip install -r requirements.txt


迁移数据库
python manage.py makemigrations
python manage.py migrate


启动
python manage.py runserver

针对敏感信息.gitignore忽略了需要自行调配

