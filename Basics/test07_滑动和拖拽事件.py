from appium import webdriver
import time

desired_cops = dict()
# 手机参数
desired_cops['platfromName'] = 'Android'
desired_cops['platfromVersio1n'] = '10'
desired_cops['deviceName'] = '192.168.56.101:5555'
# 应用参数
desired_cops['appPackage'] = 'com.android.settings'
desired_cops['appActivity'] = '.Settings'
desired_cops['unicodeKeyboard']: True # 使用自带输入法，输入中文时填True
desired_cops['resetKeyboard']: True  # 执行完程序恢复原来输入法

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cops)
# 从100,2000 到  100  1000
driver.swipe(100,2000,100,1000)
# 从100,2000 到  100  100  持续5秒
driver.swipe(100,2000,100,100,5000)


driver.quit()