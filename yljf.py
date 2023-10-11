"""
0 7 * * * yljf.py
new Env("伊利积分")
env add yljf_token
"""
# !/usr/bin/env python3
# coding: utf-8
import os
import requests
import urllib3
import mytool
from notify import send
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
title = '伊利积分'
tokenName = 'yljf_token'
msg = ''


class yljf():
    def __init__(self, data):
        self.headers = {
            'Host': 'msmarket.msx.digitalyili.com',
            'Connection': 'keep-alive',
            'access-token': data,
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/8447',
            'tenant-id': '1678248156573593602',
            'Accept': '*/*',
            'Referer': 'https://servicewechat.com/wx1fb666a33da7ac88/13/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.sec = requests.session()
        self.sec.headers = self.headers
        pass

    def login(self):
        global msg
        rj = self.sec.post('https://msmarket.msx.digitalyili.com/gateway/api/member/daily/sign', json={}).json()
        if rj['status'] == True:
            msg = f"登录成功\n获得积分：{rj['data']['dailySign']['bonusPoint']}"
        else:
            msg = f"登录失败\n" + json.dumps(rj, ensure_ascii=False)
        print(msg)
        send(title, msg)


if __name__ == '__main__':
    # DEBUG
    if os.path.exists('debug.py'):
        import debug

        debug.setDebugEnv()

    if mytool.getlistCk(f'{tokenName}') is None:
        print(f'请检查你的变量名称 {tokenName} 是否填写正确')
        exit(0)
    else:
        for i in mytool.getlistCk(f'{tokenName}'):
            yljf(i).login()
