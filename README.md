官方文档：https://docs.djangoproject.com/zh-hans/3.2/topics/auth/

流程设计：

<img src="C:\Users\11\AppData\Roaming\Typora\typora-user-images\image-20230715225801132.png" alt="image-20230715225801132" style="zoom:50%;" />



数据库设计：

用户：id username password

```python
class UserProfile(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
```

凭证：用户id 用户username拼接password的md5加密

```python
class VerifyLogin(models.Model):
    username = models.CharField(max_length=255)
    verifying = models.CharField(max_length=255)
```

一个非常简单的登录demo 

估计后面还会补充restful接口相关的demo



