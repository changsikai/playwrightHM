import csv
import wx
import ddddocr
import requests
from playwright.sync_api import Playwright, sync_playwright, expect



# def name():
#     with open("shuju.csv") as file_name:
#         file_read = csv.reader(file_name)
#         array = list(file_read)
#     print(array)
#     return array
result=0
def run(playwright: Playwright) -> None:
    with open("shuju.csv") as file_name:
        file_read = csv.reader(file_name)
        array = list(file_read)
        for num in array:
            response = requests.get(
                "http://v2.api.juliangip.com/dynamic/getips?num=1&pt=1&result_type=text&split=1&trade_no=1950270426393628&sign=6e49f39a3bfc94c630187968f8ec4a3c")
            rec = response.text
            # print(rec["proxy"])
            print(rec)
            print(num[0] + "密码" + num[1])

            browser = playwright.chromium.launch(headless=False, proxy={"server": "http://" + rec + ""
                                                                        })
            context = browser.new_context()
            context.set_default_navigation_timeout(100000)  # 超时时间是10s
            # page.set_default_timeout(10000)  # 超时时间是10s

            page = context.new_page()
            page.goto("https://toptoon.monster/?pid=MjEzODgw")
            page.get_by_role("button").filter(has_text="用户中心").click()
            page.get_by_role("link", name="会员注册").click()
            page.get_by_role("textbox", name="请输入会员帐号").click()
            page.get_by_role("textbox", name="请输入会员帐号").fill(num[0])
            page.get_by_role("textbox", name="请输入会员帐号").press("Tab")
            page.get_by_role("textbox", name="请输入密码").fill(num[1])
            page.get_by_role("textbox", name="请输入密码").press("Tab")
            page.locator("form").filter(has_text="登入 会员注册 邮箱/账户注册 储存帐号 自动登入 同意使用条款 同意个人资料保护方针 会员注册").locator(
                "#captcha").screenshot(path="screenshot.png")
            ocr = ddddocr.DdddOcr()
            with open('screenshot.png', 'rb') as f:
                img_bytes = f.read()
            result = ocr.classification(img_bytes)
            print(result)

            app = wx.App(False)
            frame = wx.Frame(None, wx.ID_ANY, u"带有图标的窗口")
            frame.SetTitle('wxPython控件演示')
            # self.SetIcon(wx.Icon('res/wx.ico'))
            frame.SetSize((460, 450))
            frame.Center()

            # 创建一个面板，用于放置控件
            panel = wx.Panel(frame, -1)
            # 在x=20，y=20的位置，创建静态文本控件
            st = wx.StaticText(panel, -1, '请输入正确的验证码', pos=(20, 20))
            # 在x=300，y=20的位置，创建静态图片
            bmp = wx.Bitmap('screenshot.png')
            sb = wx.StaticBitmap(panel, -1, bmp, pos=(280, 10))
            # 在x=20, y=50的位置，创建文本输入框，指定输入框的宽度为260像素，高度默认
            tc1 = wx.TextCtrl(panel, -1, value=result, pos=(20, 50), size=(260, -1))
            # 在x=120，y=190的位置，创建按钮
            btn = wx.Button(panel, -1, '按钮', pos=(150, 190))

            def on_left_down(btn):
                """左键按下事件函数"""

                print(btn)

            btn.Bind(wx.EVT_LEFT_DOWN, on_left_down(tc1))

            frame.Show()  # 显示窗主口
            app.MainLoop()  # 应用程序进入事件处理主循环

            page.get_by_role("textbox", name="验证码").fill(input("请输入验证码"))

            page.get_by_role("button", name="会员注册").click()
            # page.get_by_role("button").filter(has_text="用户中心").click()
            # page.get_by_role("link", name="登入").click()
            # page.get_by_role("textbox", name="请输入会员帐号").click()
            # page.get_by_role("textbox", name="请输入会员帐号").fill(num[0])
            # page.get_by_role("textbox", name="请输入会员帐号").press("Tab")
            # page.get_by_role("textbox", name="请输入密码").click()
            # page.get_by_role("textbox", name="请输入密码").fill(num[1])
            # page.get_by_role("textbox", name="请输入密码").press("Tab")
            # page.get_by_role("textbox", name="验证码").fill(input("请输入验证码"))
            # page.get_by_role("button", name="登入").click()
            # page.get_by_role("button").filter(has_text="用户中心").click()
            # page.get_by_role("link", name="登出").click()
            # page.get_by_role("button", name="登出").click()

            # ---------------------

            context.close()
            browser.close()


with sync_playwright() as playwright:
    run(playwright)
