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

# 获取手机分辨率
print(driver.get_window_size())

# 截图
driver.get_screenshot_as_file("/dawda/dwad/1.png")

# 获取当前的网络
print(driver.network_connection)

# 设置当前网络
driver.set_network_connection(1)

# 发送键到设备
# 三下加音量3下减音量
driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(25)
driver.press_keycode(25)
driver.press_keycode(25)

# 打开通知栏
driver.open_notifications()
# 关闭通知栏

driver.quit()