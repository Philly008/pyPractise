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

数据迁移：  
python manage.py migrate  

创建登录Admin后台的管理员账号:  
python manage.py createsuperuser  

如果想限制某个视图函数必须登录才能访问，只需在函数前面加上@login_required即可。  
from django.contrib.auth.decorators import login_required  

Django 提供完善的模型（model） 层主要用来创建和存取数据， 不需要我们直接对数据库操作。  
Django 模型基础知识：  
每个模型是一个 Python 类， 继承 django.db.models.model 类。  
该模型的每个属性表示一个数据库表字段。

python manage.py makemigrations sign   

shell模式操作Django模型，操作数据库表：  
python manage.py shell  
``` 
>>> from sign.models import Event, Guest    # 导入表
>>> Event.object.all()  # 查看表中的所有对象
>>>  Event.objects.create(id=3,name='红米MAX发布会',limit=2000,status=True,address='北京会展中心',start_time=datetime(2019,3,7,11,0,0))  # 插入数据
>>> e1 = Event.objects.get(name='红米MAX发布会') # 查询数据
>>> e1.status
>>> e2 = Event.objects.filter(name__contains='发布会') # 模糊查询  
>>> e1.delete() # 删除数据
>>> Guest.objects.select_for_update().filter(phone='111').update(realname='22')  # 更新数据
```
MySQL数据库操作:  
``` 
service mysqld start;    # 启动数据库
mysql -uroot -p123456;   # 登录数据库
show databases; # 查看所有数据库
use test;   # 切换到数据库test
show tables;    # 查看表
show global variables like 'port';  # 查看mysql端口号
create database guest character set utf8;   # 创建数据库
```
安装PyMySQL驱动:  
pip install PyMySQL  

在../guest/__init__.py目录下添加：  
import pymysql  
pymysql.install_as_MySQLdb()    # 指定用PyMySQL驱动  

前端框架Bootstrap提供了优雅的HTML和CSS规范，它即是由动态CSS语言Less写成。  
pip install django-bootstrap3  

{%%}为Django的模板标签，Django的模板语言将会在该标签下编写。  
{{}}用于定义显示变量  
{% for event in events %}  
{% endfor %}

分页器：  
``` 
python manage.py shell
from django.core.paginator import Paginator  # 导入Paginator类
from sign.models import Guest  # 导入Guest下的所有表
guest_list = Guest.objects.all()  # 查询Guest表的所有数据
p = Paginator(guest_list,2)  # 创建每页2条数据的分页器
p.count  # 查看共有多少条数据
p.page_range  # 查看共分多少页
page1 = p.page(1)  # 获取第1页的数据
page1  # 当前第几页
page1.object_list  # 当前页的对象
for p in page1: # 循环打印第1页的嘉宾的realname
  print(p.realname)
page1.start_index()  # 本页的第一条数据
page1.end_index()  # 本页的最后一条数据
page1.has_previous()  # 是否有上一页
page1.has_next()  # 是否有下一页
page1.previous_page_number()  # 上一页是第几页
page1.next_page_number()  # 下一页是第几页
page1.has_other_pages()  # 是否有其它页
page1.previous_page_number()  # 前一页是第几页
```
一般单元测试框架完成以下几件事：  
- 提供用例组织与执行
- 提供丰富的比较方法
- 提供丰富的日志

单元测试：unittest  
HTTP接口自动化测试：unittest+Requests  
Web UI自动化测试：unittest+Selenium  
移动自动化测试：unittest+Appium  

``` 
首先， 通过 import 导入 unittest 单元测试框架。
创建 CountTest 类继承 unittest.TestCase 类。
setUp()和 tearDown()在单元测试框架中比较特别， 它们分别在每一个测试用例的开始和结束执行。setUp()
方法用于测试用例执行前的初始化工作， 例如初始化变量、 生成数据库测试数据、 打开浏览器等。 tearDown()
方法与 setUp()方法相呼应， 用于测试用例执行之后的善后工作， 例如清除数据库测试数据、 关闭文件、 关闭
浏览器等。
unittest 要求测试方法必须以“test” 开头。 例如， test_add、 test_sub 等。
接下来， 调用 unittest.TestSuite()类中的 addTest()方法向测试套件中添加测试用例。 简单的可以将测试套
件理解成运行测试用例的集合。
通过 unittest.TextTestRunner()类中的 run()方法运行测试套件中的测试用例。
如果想默认运行当前测试文件下的所有测试用例， 可以直接使用 unittest.main()方法。 那么 main()方法在
查找测试用例时按照两个规则。 首先， 该测试类必须继承 unittest.TestCase 类； 其次， 该测试类下面的方法必
须以“test” 开头。
```
创建Django应用时默认生成了tests.py文件。  
运行测试:  
python manage.py test  
运行sign应用下的tests.py测试文件：  
python manage.py test sign.tests  
运行ModelTest测试类下面的test_event_models测试方法：  
python manage.py test sign.tests.ModelTest.test_event_models  
使用-p参数模糊匹配测试文件：  
python manage.py test -p test*.py  
客户端测试是一个Python类，充当一个虚拟的网络浏览器，测试视图层。  
``` 
python manage.py shell
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client
c = Client()
response = c.get('/index/')
response.status_code
```
HTTP协议的主要特点：  
1. 支持客户/服务器模式
2. 灵活
3. 无连接
4. 无状态  

接口自动化测试过程：  
1. 接口测试项目先向测试数据库中插入测试数据
2. 调用被测系统接口
3. 系统接口根据传参向测试数据库中进行查询并得到信息
4. 将查询结果组装成一定格式的数据，并返回给被调用者
5. 通过单元测试框架断言接口返回的数据，并生成测试报告

Requests库：  
pip install requests  
``` 
>>> import requests
>>> r = requests.get('https://api.github.com/user',auth=('Philly008','l'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf-8'
>>> r.encoding
'utf-8'
>>> r.text
>>> r.json()
```
pyrequests框架：  
db_fixture/:初始化接口测试数据  
interface/:用于编写接口自动化测试用例  
report/:生成接口自动化测试报告  
db_config.ini:数据库配置文件  
HTMLTestRunner.py:unittest单元测试框架扩展，生成HTML格式的测试报告  
run_tests.py:执行所有接口测试用例  

如何批量执行不同文件目录下的用例呢？  
unittest提供了discover()方法
















