import requests
import json


class base:
    def __init__(self, u, t):
        self.url = u
        self.token = t

    def post(self, f, p):
        data = {
            "function": f,
            "token": self.token,
            "params": p

        }
        # print(data)

        data = json.dumps(data)
        r = requests.post(url=self.url, data=data)

        return r.json()

    def post_data(self, f, p):
        return self.post(f, p)


class Send(base):
    def __init__(self, u, t):
        base.__init__(self, u, t)

    def div(self, f, p):
        """
        do it self
        :param f:
        :param p:
        :return:
        """
        return base.post_data(self, f, p)

    def get_friend_list(self, qq_number):
        f = "Api_GetFriendList"
        p = {
            "c1": qq_number,

        }
        return base.post_data(self, f, p)

    def get_group_list(self, qq_number):
        f = "Api_GetGroupList"
        p = {
            "c1": qq_number,

        }
        return base.post_data(self, f, p)

    def get_group_member_list(self, qq_number, group_number):
        f = "Api_GetGroupMemberList_C"
        p = {
            "c1": qq_number,
            "c2": group_number

        }
        return base.post_data(self, f, p)

    def get_admin_list(self, qq_number, group_number):
        f = "Api_GetAdminList"
        p = {
            "c1": qq_number,
            "c2": group_number

        }
        return base.post_data(self, f, p)

    def send_msg(self, qq_number, get_qq_number, content):
        f = "Api_SendMsg"
        p = {
            "c1": qq_number,
            "c2": "1",
            "c3": "",
            "c4": get_qq_number,
            "c5": content,

        }
        return base.post_data(self, f, p)

    def send_other_msg(self, qq_number, other_qq_number, content, msg_type):
        f = "Api_SendMsg"
        p = {
            "c1": qq_number,
            "c2": msg_type,
            "c3": other_qq_number,
            "c4": "",
            "c5": content,

        }
        return base.post_data(self, f, p)


class tool:

    @staticmethod
    def python_to_json(content):
        return json.dumps(content)

    @staticmethod
    def json_to_python(content):
        return json.loads(content)

    @staticmethod
    def qq_head_portrait(qq_number):
        d_json = {'success': True, 'code': 200, "url": f"http://q1.qlogo.cn/g?b={qq_number}&nk=12345677&s=640"}

        return d_json


# bot = Send("http://localhost:8889/MyQQHTTPAPI", "666")
#
# send = bot.div("Api_GetCoverPic", {"c1": "3414744631", "c2": "2696047693"})
# print(send)
