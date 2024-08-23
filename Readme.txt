生成本地数据库文件
python manage makemigrations

生成数据表
python manage migrate


启动服务 #默认启动8000端口
python manage runserver

可以添加配置项
python manage runserver 0.0.0.0:3000
