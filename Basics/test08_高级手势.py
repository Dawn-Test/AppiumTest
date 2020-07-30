from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction

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

# =========轻敲========
# 找到要点击的元素
wlan = driver.find_element_by_xpath("//*[@text='wlan']")
# 1.创建touchaction对象
touch_action = TouchAction(driver)
# 2.调用想要执行的动作
touch_action = touch_action.tap(wlan)
# 3.使用perform执行动作
touch_action.perform()
# 简写
TouchAction(driver).tap(wlan).perform()

driver.quit()

# ========按下和抬起
TouchAction(driver).press(x=650,y=650).perform()
time.sleep(2)
TouchAction(driver).press(x=650,y=650).release().perform()

# ====等待
TouchAction(driver).tap(x=650,y=650).perform()
time.sleep(2)
TouchAction(driver).press(x=650,y=650).perform().wait(2000).release().perform()

# =====长按
TouchAction(driver).tap(x=650,y=650).perform()
time.sleep(2)
TouchAction(driver).long_press(x=650,y=650,duration=3000).perform()

# ====移动
TouchAction(driver).move_to(x=1,y=21).move_to(x=12,y=2223).move_to(x=212,y=2123).release().perform()