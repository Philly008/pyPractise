安装  pip install django  
安装指定版本 pip install django==1.10.3  
查看  pip show django

进入项目目录输入 django-admin  可以查看相关命令  

创建guest项目：  
django-admin startproject guest  
```
guest/__init__.py： 一个空的文件， 用它标识一个目录为 Python 的标准包。
guest/settings.py： Django 项目的配置文件， 包括 Django 模块应用配置， 数据库配置， 模板配置等。
guest/urls.py： Django 项目的 URL 声明。
guest/wsgi.py： 为 WSGI 兼容的 Web 服务器服务项目的切入点。
manage.py： 一个命令行工具， 可以让你在使用 Django 项目时以不同的方式进行交互。
```
进入guest项目目录：  
cd guest  
查看manage所提供的命令：  
python manage.py  
https://docs.djangoproject.com/en/2.1/ref/django-admin/  
创建sign项目：  
python manage.py startapp sign  
``` 
migrations/： 用于记录 models 中数据的变更。
admin.py： 映射 models 中的数据到 Django 自带的 admin 后台。
apps.py： 在新的 Django 版本中新增， 用于应用程序的配置。
models.py： 创建应用程序数据表模型（对应数据库的相关操作） 。
tests.py： 创建 Django 测试。
views.py： 控制向前端显示哪些数据。
```
运行项目,默认启动8000端口：  
python manage.py runserver  
指定IP地址和端口号运行项目：  
python manage.py runserver 127.0.0.1:8001  
打开浏览器，访问：http://127.0.0.1:8001/  

Django 里更关注的是模型（Model） 、 模板(Template)和视图（Views） ，
Django 也被称为 MTV 框架 。 在 MTV 开发模式中：  
M 代表模型（Model） ， 即数据存取层。 该层处理与数据相关的所有事务： 如何存取、 如何验证有效  
T 代表模板(Template)， 即表现层。 该层处理与表现相关的决定： 如何在页面或其他类型文档中进行显
示。  
V 代表视图（View） ， 即业务逻辑层。 该层包含存取模型及调取恰当模板的相关逻辑。 你可以把它看
作模型与模板之间的桥梁。

CSRF(Cross-Site Request Forgery)跨站请求伪造漏洞？  
Django 针对 CSRF 的保护措施是在生成的每个表单中放置一个自动生成的令牌， 通过这个令牌判断 POST
请求是否来自同一个网站。  
“模板标签”添加CSRF令牌：{% csrf_token %}  























