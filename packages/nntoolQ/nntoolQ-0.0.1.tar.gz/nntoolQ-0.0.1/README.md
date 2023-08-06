# nn-pip-tools
工具集合

### 安装(Python 版本>=3.8.0)
```
pip install --upgrade nntoolQ
```

### 使用

#### 发送邮件
```
from tmtool.tools import Tool
tool = Tool()

tool.mail_from_user_host = '发件地址host'
tool.mail_from_user = '发件人邮箱号'
tool.mail_from_user_pwd = '发件人密码'

tool.send_mail_msg(to_user='收件人邮箱地址（这里是列表，可填写多个）', title='邮件标题', content='邮件内容')
```
