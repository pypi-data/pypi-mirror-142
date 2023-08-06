import requests
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from http.server import HTTPServer, BaseHTTPRequestHandler


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


news_data_json = ""


class news:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    class _request(BaseHTTPRequestHandler):

        def do_POST(self):
            content_length = int(self.headers['content-length'])
            news_data_byte = self.rfile.read(content_length)
            global news_data_json

            news_data_json = json.loads(news_data_byte)

            data = {
                'result_code': '',
                'result_desc': 'Success',
                'timestamp': '',
                'data': {}
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
            return news_data_json

    def run(self):
        host = (self.host, self.port)
        HTTPServer(host, self._request).handle_request()
        return news_data_json


# n = news('127.0.0.1', 5000)
# a = n.run()
# print(a)
