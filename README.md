# SummerProject
这是一个微微微小项目的后端雏形，利用django和django rest framework搭建的临床康复量表的WebAPP后端API。

##安装
确保具有python环境，安装必要的包,

```
(sudo) pip install django
(sudo) pip install djangorestframework
```

```
cd SummerProject
python manage.py makemigrations
python manage.py makemigrations backend
python manage.py migrate
python manage.py runserver
```

用浏览器访问 localhost:8000 即可

###数据库模型构建

  采用sqlite3引擎

####初步构想

- Patient
    - name(char)
    - idnumber(char)
    - gender(char)
    - age(integer)
    - owner(ForeignKey of auth.User)
- Project
    - name
    - patient(ManyToMany to Patient, through DateAndValue)
- DateAndValue
    - patient(foreign key )
    - project(foreign key)
    - date(auto_now)
    - value(integer)

其中Patient和Project通过DateAndValue建立多对多关系</br>
Date时，Patient参与Project，获得Value分。

###视图

采用django rest framework自带的通用视图 ViewSet，自带了 put get post delete等方法。

###授权管理

Patient模型中，加入了Owner作为User的外键。在序列化生成器中在PatientSerializer中加入owner作为只读Field，且用owner.username作为源，之后在视图中的显示以及反向查找中，就以用户名作为依据，因为用户名在User中是Unique的。</br>
由于加入了授权管理，所以可能需要创建一个超级管理员，终端中输入

```
python manage.py createsuperuser
```

在`localhost:8000/api-auth/login/`中可以进行登录


#####自定义了Permission

Patient中 IsOwnerOrReadOnly 即只有Owner才可以采取PUT方法，对非Owner的User只读</br>

Project没有定义权限，即所有人可以Post（考虑在之后修改为只有SuperUser才能修改，其与用户可以提交改动申请，访客只读）</br>

DateAndValue权限设置任在努力中，因其涉及到Patient Project 和 DateAndValue本身的User，理想状态是如果当前request.User==patient.owner，才能采取不安全的申请方法，其余只读，但逻辑仍在完善中。

###Url分配

采用了router自动分配，使代码非常简洁
