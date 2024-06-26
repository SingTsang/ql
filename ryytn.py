"""
cron: 0 7 * * * ryytn.py
new Env("微信小程序-认养一头牛商城")
env add ryytn_data

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""

import json
import os
import traceback
import requests
import urllib3

import ApiRequest
import mytool

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

title = '微信小程序-认养一头牛商城'
tokenName = 'ryytn_data'


class ryytn(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'www.milkcard.mall.ryytngroup.com',
            'Connection': 'keep-alive',
            'xweb_xhr': '1',
            'X-Auth-Token': data,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309071d)XWEB/8461',
            'Accept': '*/*',
            'Referer': 'https://servicewechat.com/wx0408f3f20d769a2f/234/page-frame.html',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def login(self):
        response = self.sec.post('https://www.milkcard.mall.ryytngroup.com/mall/xhr/task/checkin/save', json={}).json()
        print(response)


if __name__ == '__main__':
    # DEBUG
    # if os.path.exists('debug.py'):
    #     import debug
    #
    #     debug.setDebugEnv()
    #
    # if mytool.getlistCk(f'{tokenName}') is None:
    #     print(f'请检查你的变量名称 {tokenName} 是否填写正确')
    #     exit(0)
    # else:
    #     for i in mytool.getlistCk(f'{tokenName}'):
    #         ryytn(i).login()
    ApiRequest.ApiMain(['login']).run(tokenName, ryytn)