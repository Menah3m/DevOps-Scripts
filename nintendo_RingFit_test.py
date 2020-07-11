"""
查看 健身环大冒险 库存情况脚本

"""

import requests
import yagmail
from lxml import etree
import json

EMAIL_USER = '' # 发件人的邮箱地址
EMAIL_PASSWORD ='' #授权码
RECIPIENTS = []  #收件人的邮箱列表

url = 'https://store.nintendo.co.jp/item/HAC_Q_AL3PA.html?utm_source=www.nintendo.co.jp&utm_medium=referral'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
}




r = requests.get(url=url, headers=headers).content

html = etree.HTML(r)
result = html.xpath('//*[@id="itemDetail"]/div[2]/div[5]/form/div[2]/div/div/p/text()')

if result[0] == '品切れ':
    with yagmail.SMTP(user=EMAIL_USER, password=EMAIL_PASSWORD, host='smtp.163.com') as yag:
        content = """
            健身大冒险现在的库存状况是：[{}]。
            
            赶快下单吧！！
            任天堂官网：https://store.nintendo.co.jp/
            健身大冒险购买页面：https://store.nintendo.co.jp/item/HAC_Q_AL3PA.html?utm_source=www.nintendo.co.jp&utm_medium=referral
        """.format(result[0])
        for recipient in RECIPIENTS:
            yag.send(recipient,subject="健身大冒险库存更新了！", contents=content)

