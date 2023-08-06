# toolspro

工具包

### 安装(Python 版本>=3.6.8)
```
pip install --upgrade toolsPro
```

### 使用

#### 发送邮件
```
from toolspro.tools import Tool
tool = Tool()

tool.mail_from_user_host = '发件地址host'
tool.mail_from_user = '发件人邮箱号'
tool.mail_from_user_pwd = '发件人密码'

tool.send_mail_msg(to_user='收件人邮箱地址（这里是列表，可填写多个）', title='邮件标题', content='邮件内容')
```
