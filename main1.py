import playwright
from playwright.sync_api import Playwright, sync_playwright, expect

browser = playwright.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()
page.goto("https://toptoon.monster/?pid=MjEzODgw")
page.get_by_role("button").filter(has_text="用户中心").click()
page.get_by_role("link", name="会员注册").click()
page.get_by_role("textbox", name="请输入会员帐号").click()
page.get_by_role("textbox", name="请输入会员帐号").fill("1123574@qq.com")
page.get_by_role("textbox", name="请输入会员帐号").press("Tab")
page.get_by_role("textbox", name="请输入密码").fill("123456")
page.get_by_role("textbox", name="请输入密码").press("Tab")
page.get_by_role("textbox", name="验证码").fill(input("请输入验证码"))
page.get_by_role("button", name="会员注册").click()
page.get_by_role("button").filter(has_text="用户中心").click()
page.get_by_role("link", name="登入").click()
page.get_by_role("textbox", name="请输入会员帐号").click()
page.get_by_role("textbox", name="请输入会员帐号").fill("1123574@qq.com")
page.get_by_role("textbox", name="请输入会员帐号").press("Tab")
page.get_by_role("textbox", name="请输入密码").click()
page.get_by_role("textbox", name="请输入密码").fill("123456")
page.get_by_role("textbox", name="请输入密码").press("Tab")
page.get_by_role("textbox", name="验证码").fill(input("请输入验证码"))
page.get_by_role("button", name="登入").click()
page.get_by_role("button").filter(has_text="用户中心").click()
page.get_by_role("link", name="登出").click()
page.get_by_role("button", name="登出").click()

# ---------------------
context.close()
browser.close()
