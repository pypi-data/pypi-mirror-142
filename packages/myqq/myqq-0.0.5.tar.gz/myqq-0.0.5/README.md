# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://github.com/maisge/myqq/blob/main/README.md)
to write your content.

###取好友列表 [get_friend_list("机器人qq号")]
```python
# 导入库
from myqq import send
# 新建机器人
bot = send.Send("http://localhost:8889/MyQQHTTPAPI", "666")
# 取好友列表
f_list = bot.get_friend_list("3414744631")
# 输出
print(f_list)
```

