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
        print(data)

        data = json.dumps(data)
        r = requests.post(url=self.url, data=data)

        return r.json()

    def post_data(self, f, p):
        return self.post(f, p)


class Send(base):
    def __init__(self, u, t):
        base.__init__(self, u, t)

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
            "c2":group_number

        }
        return base.post_data(self, f, p)

    def get_admin_list(self, qq_number, group_number):
        f = "Api_GetAdminList"
        p = {
            "c1": qq_number,
            "c2": group_number

        }
        return base.post_data(self, f, p)


# aa = Send("http://localhost:8889/MyQQHTTPAPI", "666")
#
#
# bbb = aa.get_group_member_list("3414744631", "699790151")
# print(bbb)
#



# def sendmsg(postqq, _type, group="", getqq="", text=""):
#     function = "Api_SendMsg"
#     params = {
#         "c1": postqq,
#         "c2": _type,
#         "c3": group,
#         "c4": getqq,
#         "c5": text,
#     }
#     dowork(function, params)
