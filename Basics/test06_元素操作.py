from appium import webdriver
import time

desired_cops = dict()
# 手机参数
desired_cops['platfromName'] = 'Android'
desired_cops['platfromVersio1n'] = '5.1.1'
desired_cops['deviceName'] = '192.168.56.101:5555'
# 应用参数
desired_cops['appPackage'] = 'com.android.settings'
desired_cops['appActivity'] = '.Settings'
desired_cops['unicodeKeyboard']: True # 使用自带输入法，输入中文时填True
desired_cops['resetKeyboard']: True  # 执行完程序恢复原来输入法

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cops)
# 点击元素
# driver.find_element_by_id("com.android.settings").click()

# 输入内容
driver.find_element_by_id("com.android.settings").click()
driver.find_element_by_id("com.android.setting.text").send_keys("hello")
driver.find_element_by_id("com.android.setting.text").clear()
driver.find_element_by_id("com.android.setting.text").send_keys("你好")

# 获取文本内容
eles = driver.find_element_by_id("xx")
for i in eles:
    print(i.text)

# 获取元素的位置和大小
search = driver.find_element_by_id("com.android")
print(search.location)
print(search.size)

# 获取元素的属性值
el =driver.find_element_by_id("com.android.aa")
for i in el:
    print(i.get_attribute("enabled"))

time.sleep(3)
driver.quit()