import csv
from tkinter import *

import ddddocr
import requests
from playwright.sync_api import Playwright, sync_playwright, expect

# def name():
#     with open("shuju.csv") as file_name:
#         file_read = csv.reader(file_name)
#         array = list(file_read)
#     print(array)
#     return array
result = 0


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
            # headless = False,
            browser = playwright.chromium.launch(headless=False, proxy={"server": "http://" + rec + ""
                                                                        })
            context = browser.new_context()
            context.set_default_navigation_timeout(100000)  # 超时时间是10s
            # page.set_default_timeout(10000)  # 超时时间是10s

            page = context.new_page()
            page.set_default_timeout(100000)
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
            # print(result)
            root = Tk()
            root.geometry('600x450')
            picture = PhotoImage(file="screenshot.png")  # 必须是真正的gif图片，改变图片的格式改不了图片的本质，无法运行
            label3 = Label(root, text='图片', image=picture, compound='left', relief=SUNKEN)
            label3.grid(row=2, column=5)
            entry = Entry(root, fg='blue', bg='pink', width=20, bd=4)
            entry.grid()
            entry.insert(1, result)

            def hit():
                print(entry.get())
                page.get_by_role("textbox", name="验证码").fill(entry.get())
                page.get_by_role("button", name="会员注册").click()
                context.close()
                browser.close()
                root.destroy()
            button = Button(root, text='点击', width=12, height=2, command=hit)
            button.grid()
            root.mainloop()


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
