# packageManager
依赖
pymysql==0.9.3
Pillow==5.4.1
xlrd==1.2.0
xpinyin==0.5.6
FtpLibrary==1.1
requests==2.21.0
numpy==1.6.0
包的管理
- 创建迁移文件
> python manage.py makemigrations

- 通过迁移文件生成表
> python manage.py migrate

- 运行项目
python3 manage.py runserver 127.0.0.1:8001

# release
#docker run -d  -p 443:443 -p 80:80 -p 222:22 --name gitlab --restart always -v /home/gitlab/config:/etc/gitlab -v /home/gitlab/logs:/var/log/gitlab -v /home/gitlab/data:/var/opt/gitlab gitlab/gitlab-ce

#docker run -d -p 443:443 -p 80:80 -p 222:22 --name gitlab --restart always -v /home/gitlab/config:/Users/yu/gitlabconfig -v /home/gitlab/logs:/Users/yu/gitlablog -v /home/gitlab/data:/Users/yu/gitlabdata gitlab/gitlab-ce