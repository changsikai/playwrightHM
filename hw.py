from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://talentstore.shixizhi.huawei.com/")
    page.goto("https://talentstore.shixizhi.huawei.com/portal/1513486475269996546?sxz-lang=zh_CN")
    page.get_by_placeholder("帐号名/邮箱/手机号/W3帐号").click()
    page.get_by_placeholder("帐号名/邮箱/手机号/W3帐号").fill("18574176641")
    page.get_by_placeholder("密码").click()
    page.get_by_placeholder("密码").fill("QQ13569394808k@")
    page.get_by_label("记住用户名").check()
    page.get_by_role("button", name="登录").click()
    page.goto("https://talentstore.shixizhi.huawei.com/login/index?redirect=https%3A%2F%2Ftalentstore.shixizhi.huawei.com%2Fcourse%2F1513486475269996546%2Fapplication-view%3FcourseId%3D1669645863046729730%26appId%3D542834252854403072%26appType%3D3%26activeIndex%3D0%26sxz-lang%3Dzh_CN&sxz-lang=zh_CN")
    # page.get_by_text("获取验证码").click()
    # page.get_by_placeholder("短信验证码").click()
    # page.get_by_placeholder("短信验证码").fill(input("验证码"))
    # page.get_by_role("button", name="确定").click()
    page.get_by_text("HCIP笔试考券全额代金券").click()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
