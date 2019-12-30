import time

from selenium import webdriver
import os
# driver=webdriver.Chrome()
# driver.get("http://192.168.9.121")

class Test_GMS():
    def test_login(self):
        # 确定chromedriver.exe的位置
        driver_path = os.path.join(os.path.dirname(__file__), "D:\software\Python\chromedriver.exe")
        # 打开浏览器
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()  # 最大化浏览器
        driver.set_page_load_timeout(10)  # 网页加载超时为10s
        driver.set_script_timeout(10)  # js脚本运行超时10s
        driver.implicitly_wait(10)  # 元素查找超时时间10s
        driver.get('http://192.168.9.121')
        User =driver.find_element_by_xpath("//input[@placeholder='User ID']")    # 定位UserID
        Password=driver.find_element_by_xpath("//input[@placeholder='Password']")    # 定位Pssword
        User.send_keys("Admin") # 输入UserID=Admin
        Password.send_keys("Abc123")    # 输入Pssword=Abc123
        driver.find_element_by_xpath("//input[@placeholder='Select']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[contains(text(),'Singapore')]").click() # Country下拉框点击选择Singapore
        time.sleep(1)
        driver.find_element_by_xpath("//span[contains(text(),'Sign In')]").click()  # 点击Sign In登录
        time.sleep(2)
        pass
