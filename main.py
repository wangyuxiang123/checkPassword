import json

import requests

password = 123456789
jwsession = "18fc54f85ce14ff280d919915fdab838"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json;charset=UTF-8",
    "Referer": "https://gw.wozaixiaoyuan.com/h5/mobile/basicinfo/index/my/changePassword",
    "Host": "gw.wozaixiaoyuan.com",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.23(0x1800172f) NetType/WIFI Language/zh_CN miniProgram/wxce6d08f781975d91",
    "Connection": "keep-alive",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "JWSESSION": jwsession,
    "Cookie": f"JWSESSION={jwsession}"
}

# loginUrl = f"https://student.wozaixiaoyuan.com/basicinfo/mobile/login/username?username={username}&password={password}"
# session = requests.session()
# # 请求体（必须有） body = "{}"
# body = "{}"
# response = session.post(url=loginUrl, data=body, headers=headers)
# res = json.loads(response.text)
# if res["code"] == 0:
#     print("登陆成功")
#     # 登录成功获取JWSESSION
#     print(response.headers['JWSESSION'])
#
#     headers["JWSESSION"] = response.headers['JWSESSION']

print(headers)
resetUrl = f"https://gw.wozaixiaoyuan.com/basicinfo/mobile/my/changePassword?newPassword={password}&oldPassword={password}&code="
res = requests.post(url=resetUrl, headers=headers)
print(res.text)
new_JWSESSION = res.headers["JWSESSION"]
print("jwsession-->", new_JWSESSION)
with open("jwsession.txt", "w") as f:
    f.write(new_JWSESSION)

