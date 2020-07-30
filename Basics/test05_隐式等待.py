from appium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

desired_cops = dict()
# 手机参数
desired_cops['platfromName'] = 'Android'
desired_cops['platfromVersio1n'] = '10'
desired_cops['deviceName'] = '192.168.56.101:5555'
# 应用参数
desired_cops['appPackage'] = 'com.android.settings'
desired_cops['appActivity'] = '.MainSettings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cops)

# ========隐式等待=======
driver.implicitly_wait(10)

print("----准备找返回点击")
driver.find_element_by_xpath("//*[@content-desc='收起']").click()
print("----点完了")


# ========显式等待==========
print("----准备找返回点击")
wait=WebDriverWait(driver, 5)
back_button = wait.until(lambda x:x.find_element_by_xpath("//*[@content-desc='收起']")).click()
print("----点完了")