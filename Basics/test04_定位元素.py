from appium import webdriver
import time


def init_driver():
    desired_caps = {
        'platformName': 'Android',  # 被测手机是安卓
        'platformVersion': '10',  # 手机安卓版本
        'deviceName': 'xxx',  # 设备名，安卓手机可以随意填写
        'appPackage': 'com.android.contacts',  # 启动APP Package名称
        'appActivity': '.activities.TwelveKeyDialer',  # 启动Activity名称
        'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
        'resetKeyboard': True,  # 执行完程序恢复原来输入法
        'noReset': True        # 不重置应用
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cops)


# =============定位一个元素
# 通过id定位放大镜按钮，点击
# search_button = driver.find_element_by_id("com.android")
# search_button.click()
#
# # 通过class定位定位输入框  输入hello4
# driver.find_element_by_class_name("xxxx").send_keys("hello")
#
# # 通过xpach定位定位返回按钮
# driver.find_element_by_xpath("//*[@content-desc='收起']").click()

# ========定位一组元素
# 通过 id形式，获取所有id为.com.android
# titles = driver.find_element_by_id("com.android")
# # print(titles)
# # print(len(titles))
# # 循环打印出来文字内容，如果点击在titles后.click（）
# for title in titles:
#     print(titles.text)
# titles[1].click()

# 通过 class_name 形式，获取所有class为 “android.xxx”
# text = driver.find_element_by_class_name("android.xxx")
# print(len(text))
# for tex in text:
#     print(text.text)
#
# # 通过 xpach 的形式，获取所有包含“设”的元素 ，并打印
# eles = driver.find_element_by_xpath("//*[contains(@text='设')]")
# print(len(eles))
# for i in eles:
#     print(eles.text)

time.sleep(3)

driver.quit()
