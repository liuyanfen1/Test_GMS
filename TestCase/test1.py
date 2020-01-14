from selenium import webdriver
import os,time,pytest

# driver=webdriver.Chrome()
# driver.get("http://192.168.9.121")

class Test_GMS():
      def test_start(self):
        # 确定chromedriver.exe的位置
        driver_path = os.path.join(os.path.dirname(__file__), "D:/software/Python/chromedriver.exe")
        # 打开浏览器
        driver = webdriver.Chrome(driver_path)
        driver.maximize_window()  # 最大化浏览器
        driver.set_page_load_timeout(10)  # 网页加载超时为10s
        driver.set_script_timeout(10)  # js脚本运行超时10s
        driver.implicitly_wait(10)  # 元素查找超时时间10s
        return driver

      def test_login(self):
        driver=self.test_start()
        driver.get('http://192.168.9.121/')
        User =driver.find_element_by_xpath("//input[@placeholder='User ID']")    # 定位UserID
        Password=driver.find_element_by_xpath("//input[@placeholder='Password']")    # 定位Pssword
        User.send_keys("Admin") # 输入UserID=Admin
        Password.send_keys("Abc123")    # 输入Pssword=Abc123
        driver.find_element_by_xpath("//input[@placeholder='Select']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[contains(text(),'Singapore')]").click() # Country下拉框点击选择Singapore
        time.sleep(1)
        driver.find_element_by_xpath("//span[contains(text(),'Sign In')]").click()  # 点击Sign In登录
        time.sleep(3)

        # Employee Data
        #  定位Employee Data 并点击
        driver.find_element_by_xpath("//div[contains(text(),'Employee Management')]").click()
        time.sleep(2)
        # # 定位租户下拉框并点击
        # driver.find_element_by_xpath("//input[@placeholder='Select']").click()
        # time.sleep(1)
        # # 定位Suez并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Suez')]").click()
        # time.sleep(1)
        # # 定位Search并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Search')]").click()
        # time.sleep(1)
        # # 定位PersonId=CC5564并点击；
        # driver.find_element_by_xpath("//span[contains(text(),'CC5564')]").click()
        # time.sleep(3)
        # # 定位Basic Information 编辑框并点击
        # BasicInformation  = driver.find_element_by_xpath("(//button[@class='el-button iconfont iconedit-2 el-tooltip el-button--text'])[1]")
        # driver.execute_script("arguments[0].click();",BasicInformation )
        # # driver.find_element_by_xpath("(//button[@class='el-button iconfont iconedit-2 el-tooltip el-button--text'])[1]").click()
        # time.sleep(1)
        # # 定位Last Name并输入内容
        # LastName=driver.find_element_by_xpath("(//input[@type='text'])[5]")
        # LastName.clear()
        # LastName.send_keys("aa")
        # time.sleep(1)
        # # 定位Middle Name并输入内容
        # MiddleName=driver.find_element_by_xpath("(//input[@type='text'])[6]")
        # MiddleName.clear()
        # MiddleName.send_keys("bb")
        # time.sleep(1)
        # # 定位FirstName并输入内容
        # FirstName=driver.find_element_by_xpath("(//input[@type='text'])[7]")
        # FirstName.clear()
        # FirstName.send_keys("cc")
        # time.sleep(1)
        # # 定位Ok按钮并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Ok')]").click()
        # time.sleep(1)

        # # 定位names栏位Add并点击
        # Add = driver.find_element_by_xpath("(//span[contains(text(),'Add')])[1]")
        # driver.execute_script("arguments[0].click();",Add)
        # time.sleep(1)
        # # 定位Effective Start Date并选择生效日
        # driver.find_element_by_xpath("(//input[@type='text'])[1]").click()
        # time.sleep(1)
        # driver.find_element_by_xpath("//span[contains(text(),'31')]").click()
        # time.sleep(1)
        # # 定位Effective Status并选择Active
        # driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        # time.sleep(1)
        # driver.find_element_by_xpath("//span[contains(text(),'Active')]").click()
        # time.sleep(1)
        # # 定位Name Type下拉框并选择Full Name
        # driver.find_element_by_xpath("(//input[@placeholder='Select'])[2]").click()
        # time.sleep(1)
        # driver.find_element_by_xpath("//span[contains(text(),'Full Name')]").click()
        # time.sleep(1)
        # # 定位Locale下拉框并选择Singapore
        # driver.find_element_by_xpath("(//input[@placeholder='Select'])[3]").click()
        # time.sleep(1)
        # driver.find_element_by_xpath("//span[contains(text(),'Singapore')]").click()
        # time.sleep(1)
        # # 定位LastName、MiddleName、FirstName并输入内容
        # LastName = driver.find_element_by_xpath("(//input[@type='text'])[5]")
        # LastName.clear()
        # LastName.send_keys("family")
        # time.sleep(1)
        # MiddleName = driver.find_element_by_xpath("(//input[@type='text'])[6]")
        # MiddleName.clear()
        # MiddleName.send_keys("are")
        # time.sleep(1)
        # FirstName = driver.find_element_by_xpath("(//input[@type='text'])[7]")
        # FirstName.clear()
        # FirstName.send_keys("we")
        # # 定位Ok按钮并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Ok')]").click()
        # time.sleep(1)
        #
        # # 定位Contact并点击
        # Contact = driver.find_element_by_xpath("(//div[contains(text(),'Contact')])[1]")
        # driver.execute_script("arguments[0].click();", Contact)
        # # driver.find_element_by_xpath("(//div[contains(text(),'Contact')])[1]").click()
        # time.sleep(1)
        # # 定位E-Mails - Add并点击
        # Add = driver.find_element_by_xpath("(//span[contains(text(),'Add')])[3]")
        # driver.execute_script("arguments[0].click();", Add)
        # # driver.find_element_by_xpath("(//span[contains(text(),'Add')])[3]").click()
        # time.sleep(1)
        # # 定位Effective Start Date并点击
        # driver.find_element_by_xpath("//input[@placeholder='Date']").click()
        # time.sleep(1)
        # # 定位日期并选择
        # driver.find_element_by_xpath("//span[contains(text(),'31')]").click()
        # time.sleep(1)
        # # 定位Effective Status并点击
        # driver.find_element_by_xpath("(//input[@placeholder='Select'])[1]").click()
        # time.sleep(1)
        # # 定位Active并选择
        # driver.find_element_by_xpath("//span[contains(text(),'Active')]").click()
        # time.sleep(1)
        # # 定位E-Mail并输入邮件地址
        # E_Mail=driver.find_element_by_xpath("(//input[@type='text'])[3]")
        # E_Mail.send_keys("carrie.liu@cdpgroupltd.com")
        # time.sleep(1)
        # # 定位E-Mail Type并点击
        # driver.find_element_by_xpath("(//input[@placeholder='Select'])[2]").click()
        # time.sleep(1)
        # # 定位Business并选择
        # driver.find_element_by_xpath("//span[contains(text(),'Business')]").click()
        # # 定位Ok并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Ok')]").click()
        # time.sleep(2)
        #
        # # Pay Data 查询
        # # 定位 Employee Management并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Employee Management')]").click()
        # time.sleep(1)
        # # 定位Pay Data并点击
        # driver.find_element_by_xpath("//li[contains(text(),'Pay Data')]").click()
        # time.sleep(1)
        # # 定位Tenant下拉框并点击
        # driver.find_element_by_xpath("(//input[@placeholder='Select'])[1]").click()
        # time.sleep(1)
        # # 定位Suez并点击选择
        # driver.find_element_by_xpath("//span[contains(text(),'Suez')]").click()
        # time.sleep(1)
        # # 定位员工CC5564并点击
        # driver.find_element_by_xpath("//span[contains(text(),'CC5564')]").click()
        # time.sleep(2)
        # # 定位Payroll Period并选择月份
        # driver.find_element_by_xpath("(//input[@placeholder='Month'])[1]").click()
        # time.sleep(1)
        # driver.find_element_by_xpath("//a[contains(text(),'Jan')]").click()
        # time.sleep(1)
        # driver.find_element_by_xpath("(//input[@placeholder='Month'])[2]").click()
        # time.sleep(1)
        # driver.find_element_by_xpath("(//a[contains(text(),'Dec')])[2]").click()
        # time.sleep(1)
        # # 定位Refresh并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Refresh')]").click()
        # time.sleep(1)
        #
        #
        # # Data Import Management 文件上传
        # # 定位Data Import Management并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Data Import Management')]").click()
        # time.sleep(1)
        # # 定位Batch Import并点击
        # driver.find_element_by_xpath("//li[contains(text(),'Batch Import')]").click()
        # time.sleep(1)
        # # # 定位Data Import按钮并点击
        # # driver.find_element_by_xpath("(//span[contains(text(),'Data Import')])[2]").send_keys("C:\Users\carrie.liu\Desktop\上传模板\Master data\suez\WTS ID - Payroll Monthly Advice Mar 2019.xlsx")
        # # time.sleep(1)


        # # 定位 Cycle Management并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Cycle Management')]").click()
        # time.sleep(1)
        # # 定位Payroll Process List并点击
        # driver.find_element_by_xpath("//li[contains(text(),'Payroll Process List')]").click()
        # time.sleep(1)
        # # 定位
        # driver.find_element_by_xpath("(//input[@placeholder='Select'])[1]").click()
        # time.sleep(1)
        # # 定位Suez并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Suez')]").click()
        # time.sleep(1)
        # # 定位Suez_WTS SG_Payroll_202301_01并点击
        # # a = driver.find_element_by_xpath("//span[contains(text(),'Suez_WTS SG_Payroll_202301_02')]")
        # # driver.execute_script("arguments[0].click();",a)
        # # driver.find_element_by_xpath("//span[contains(text(),'Suez_WTS SG_Payroll_202303_01')]").click()
        # # time.sleep(2)
        # #切换用户，定位Admin并点击
        # driver.find_element_by_xpath("//span[@class='el-dropdown-link el-dropdown-selfdefine']").click()
        # time.sleep(1)
        # # 登出，定位Sign Out并点击
        # driver.find_element_by_xpath("//div[contains(text(),'Sign Out')]").click()
        # time.sleep(1)
        # #使用Client.Test登录
        # User = driver.find_element_by_xpath("//input[@placeholder='User ID']")  # 定位UserID
        # Password = driver.find_element_by_xpath("//input[@placeholder='Password']")  # 定位Pssword
        # User.send_keys("Client.Test")  # 输入UserID=Admin
        # Password.send_keys("Abc123")  # 输入Pssword=Abc123
        # # 定位contry下拉框并点击
        # driver.find_element_by_xpath("//input[@placeholder='Select']").click()
        # time.sleep(1)
        # # Country下拉框点击选择Singapore
        # driver.find_element_by_xpath("//span[contains(text(),'Singapore')]").click()
        # time.sleep(1)
        # # Tenant输入Suez
        # Tenant=driver.find_element_by_xpath("(//input[@type='text'])[1]")
        # Tenant.send_keys("Suez")
        # time.sleep(1)
        # # 点击Sign In登录
        # driver.find_element_by_xpath("//span[contains(text(),'Sign In')]").click()  # 点击Sign In登录
        # time.sleep(3)

        # # 定位Cycle Management并点击
        # driver.find_element_by_xpath("//div[contains(text(),'Cycle Management')]").click()
        # time.sleep(1)
        # # 定位Suez_WTS SG_Payroll_202301_02并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Suez_WTS SG_Payroll_202301_02')]").click()
        # time.sleep(1)
        # # 定位Upload并点击
        # # driver.find_element_by_xpath("(//span[contains(text(),'Upload')])[2]").send_keys("D:\Documents\GMS-Carrie\GMS文件上传模板\GMS Template Documents\Payroll Detail Template\suez\Suez_WTS_ID_yyyymm_Payroll Detail Report.xlsx")
        # # time.sleep(1)
        # # 选择文件上传
        #
        # # 定位Submit并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Submit')]").click()
        # time.sleep(1)
        #
        # # 切换用户，定位CDP.Test并点击
        # driver.find_element_by_xpath("//span[@class='el-dropdown-link el-dropdown-selfdefine']").click()
        # time.sleep(1)
        # # 登出，定位Sign Out并点击
        # driver.find_element_by_xpath("//div[contains(text(),'Sign Out')]").click()
        # time.sleep(1)
        # # 使用Partner.Test登录
        # User = driver.find_element_by_xpath("//input[@placeholder='User ID']")  # 定位UserID
        # Password = driver.find_element_by_xpath("//input[@placeholder='Password']")  # 定位Pssword
        # User.send_keys("Partner.Test")  # 输入UserID=Admin
        # Password.send_keys("Abc123")  # 输入Pssword=Abc123
        # # 定位contry下拉框并点击
        # driver.find_element_by_xpath("//input[@placeholder='Select']").click()
        # time.sleep(1)
        # # Country下拉框点击选择Singapore
        # driver.find_element_by_xpath("//span[contains(text(),'Singapore')]").click()
        # time.sleep(1)
        # # 点击Sign In登录
        # driver.find_element_by_xpath("//span[contains(text(),'Sign In')]").click()  # 点击Sign In登录
        # time.sleep(3)
        #
        # # 定位Cycle Management并点击
        # driver.find_element_by_xpath("//div[contains(text(),'Cycle Management')]").click()
        # time.sleep(1)
        # # 定位Suez_WTS SG_Payroll_202301_02并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Suez_WTS SG_Payroll_202301_02')]").click()
        # time.sleep(1)
        # # 定位Submit并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Submit')]").click()
        # time.sleep(1)
        # # 切换用户，定位Partner.Test并点击
        # driver.find_element_by_xpath("//span[@class='el-dropdown-link el-dropdown-selfdefine']").click()
        # time.sleep(1)
        # # 登出，定位Sign Out并点击
        # driver.find_element_by_xpath("//div[contains(text(),'Sign Out')]").click()
        # time.sleep(1)
        # # 使用Client.Test登录
        # User = driver.find_element_by_xpath("//input[@placeholder='User ID']")  # 定位UserID
        # Password = driver.find_element_by_xpath("//input[@placeholder='Password']")  # 定位Pssword
        # User.send_keys("Client.Test")  # 输入UserID=Admin
        # Password.send_keys("Abc123")  # 输入Pssword=Abc123
        # # 定位contry下拉框并点击
        # driver.find_element_by_xpath("//input[@placeholder='Select']").click()
        # time.sleep(1)
        # # Country下拉框点击选择Singapore
        # driver.find_element_by_xpath("//span[contains(text(),'Singapore')]").click()
        # time.sleep(1)
        # # Tenant输入Suez
        # Tenant = driver.find_element_by_xpath("(//input[@type='text'])[1]")
        # Tenant.send_keys("Suez")
        # time.sleep(1)
        # # 点击Sign In登录
        # driver.find_element_by_xpath("//span[contains(text(),'Sign In')]").click()  # 点击Sign In登录
        # time.sleep(3)
        #
        # # 定位Cycle Management并点击
        # driver.find_element_by_xpath("//div[contains(text(),'Cycle Management')]").click()
        # time.sleep(1)
        # # 定位Suez_WTS SG_Payroll_202301_02并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Suez_WTS SG_Payroll_202301_02')]").click()
        # time.sleep(1)






        # # 定位Cycle Management并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Cycle Management')]").click()
        # time.sleep(1)
        # # 定位Cycle List并点击
        # driver.find_element_by_xpath("//li[contains(text(),'Cycle List')]").click()
        # time.sleep(1)
        # # 定位Add并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Add')]").click()
        # time.sleep(1)
        # # 定位Cycle Name输入框
        # CycleName=driver.find_element_by_xpath("(//input[@type='text'])[1]")
        # CycleName.send_keys("Test1")
        # time.sleep(1)
        # # 定位Role下拉框并点击
        # driver.find_element_by_xpath("(//input[@placeholder='Select'])[1]").click()
        # time.sleep(1)
        # # 定位CLIENT_HR_ROLE并选择
        # driver.find_element_by_xpath("//span[contains(text(),'CLIENT_HR_ROLE')]").click()
        # time.sleep(1)
        # #定位permission并点击
        # driver.find_element_by_xpath("(//input[@placeholder='Select'])[2]").click()
        # time.sleep(1)
        # # 定位Full Access并选择
        # driver.find_element_by_xpath("//span[contains(text(),'Full Access')]").click()
        # time.sleep(1)
        # #定位ProcessName并输入内容
        # ProcessName=driver.find_element_by_xpath("(//input[@type='text'])[4]")
        # ProcessName.send_keys("Test1")
        # time.sleep(1)
        # # 定位Comfirm To No输入框并输入内容
        # ComfirmToNo=driver.find_element_by_xpath("(//input[@type='text'])[5]")
        # ComfirmToNo.send_keys("2")
        # time.sleep(1)
        # # 定位RejectBackNo并输入内容
        # RejectBackNo=driver.find_element_by_xpath("(//input[@type='text'])[6]")
        # RejectBackNo.send_keys(" ")
        # time.sleep(1)
        # # 定位CutOffDay输入框，并输入内容
        # CutOffDay=driver.find_element_by_xpath("(//input[@type='text'])[7]")
        # CutOffDay.send_keys("02")
        # time.sleep(1)
        # # 定位Below按钮并点击
        # driver.find_element_by_xpath("//button[@class='el-button iconfont iconbelow el-tooltip el-button--text']").click()
        # time.sleep(1)
        # # 定位第2步流程的Role下拉框并点击
        # driver.find_element_by_xpath("(//input[@placeholder='Select'])[3]").click()
        # time.sleep(1)
        # # 定位CDP_USER_ROLE并选择
        # driver.find_element_by_xpath("(//span[contains(text(),'CDP_USER_ROLE')])[2]").click()
        # #定位permission下拉框并点击
        # driver.find_element_by_xpath("(//input[@placeholder='Select'])[4]").click()
        # time.sleep(1)
        # # 定位Full Access并点击
        # driver.find_element_by_xpath("(//span[contains(text(),'Full Access')])[2]").click()
        # time.sleep(1)
        # #
        # ProcessName=driver.find_element_by_xpath("(//input[@type='text'])[10]")
        # ProcessName.send_keys("Test2")
        # time.sleep(1)
        # #
        # ComfirmToNo=driver.find_element_by_xpath("(//input[@type='text'])[11]")
        # ComfirmToNo.send_keys("3")
        # time.sleep(1)
        # #
        # RejectBackNo=driver.find_element_by_xpath("(//input[@type='text'])[12]")
        # RejectBackNo.send_keys("1")
        # time.sleep(1)
        # #
        # CutOffDay=driver.find_element_by_xpath("(//input[@type='text'])[13]")
        # CutOffDay.send_keys("02")
        # time.sleep(1)
        # # 定位Below按钮并点击
        # driver.find_element_by_xpath(
        #     "(//button[@class='el-button iconfont iconbelow el-tooltip el-button--text'])[2]").click()
        # time.sleep(1)
        # # 定位第3步流程的Role下拉框并点击
        # driver.find_element_by_xpath("(//input[@placeholder='Select'])[5]").click()
        # time.sleep(1)
        # # 定位CDP_USER_ROLE并选择
        # driver.find_element_by_xpath("(//span[contains(text(),'PARTNER_USER_ROLE')])[3]").click()
        # # 定位permission下拉框并点击
        # driver.find_element_by_xpath("(//input[@placeholder='Select'])[6]").click()
        # time.sleep(1)
        # # 定位Full Access并点击
        # driver.find_element_by_xpath("(//span[contains(text(),'Full Access')])[3]").click()
        # time.sleep(1)
        # #
        # ProcessName = driver.find_element_by_xpath("(//input[@type='text'])[16]")
        # ProcessName.send_keys("Test3")
        # time.sleep(1)
        # #
        # ComfirmToNo = driver.find_element_by_xpath("(//input[@type='text'])[17]")
        # ComfirmToNo.send_keys("4")
        # time.sleep(1)
        # #
        # RejectBackNo = driver.find_element_by_xpath("(//input[@type='text'])[18]")
        # RejectBackNo.send_keys("2")
        # time.sleep(1)
        # #
        # CutOffDay = driver.find_element_by_xpath("(//input[@type='text'])[19]")
        # CutOffDay.send_keys("02")
        # time.sleep(1)
        # # 定位Below按钮并点击
        # driver.find_element_by_xpath(
        #     "(//button[@class='el-button iconfont iconbelow el-tooltip el-button--text'])[3]").click()
        # time.sleep(1)
        #
        # # 定位第4步流程的Role下拉框并点击
        # driver.find_element_by_xpath("(//input[@placeholder='Select'])[7]").click()
        # time.sleep(1)
        # # 定位CDP_USER_ROLE并选择
        # driver.find_element_by_xpath("(//span[contains(text(),'CLIENT_HR_ROLE')])[4]").click()
        # # 定位permission下拉框并点击
        # driver.find_element_by_xpath("(//input[@placeholder='Select'])[8]").click()
        # time.sleep(1)
        # # 定位Full Access并点击
        # driver.find_element_by_xpath("(//span[contains(text(),'Full Access')])[4]").click()
        # time.sleep(1)
        # #
        # ProcessName = driver.find_element_by_xpath("(//input[@type='text'])[22]")
        # ProcessName.send_keys("Test4")
        # time.sleep(1)
        # #
        # ComfirmToNo = driver.find_element_by_xpath("(//input[@type='text'])[23]")
        # ComfirmToNo.send_keys("Finish")
        # time.sleep(1)
        # #
        # RejectBackNo = driver.find_element_by_xpath("(//input[@type='text'])[24]")
        # RejectBackNo.send_keys("3")
        # time.sleep(1)
        # #
        # CutOffDay = driver.find_element_by_xpath("(//input[@type='text'])[25]")
        # CutOffDay.send_keys("02")
        # time.sleep(1)
        # # 定位Save按钮并点击
        # driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()
        # time.sleep(1)



        # Cycle Calendar Setup 新增
        # 定位Cycle Management并点击
        driver.find_element_by_xpath("//span[contains(text(),'Cycle Management')]").click()
        time.sleep(1)
        # 定位Cycle Calendar Setup 并点击
        driver.find_element_by_xpath("//li[contains(text(),'Cycle Calendar Setup')]").click()
        time.sleep(1)
        # 定位Tenant下拉框并点击
        driver.find_element_by_xpath("(//input[@placeholder='Select'])[1]").click()
        time.sleep(1)
        # 定位suez并点击
        driver.find_element_by_xpath("//span[contains(text(),'Suez')]").click()
        time.sleep(1)
        # 定位Add并点击
        driver.find_element_by_xpath("//span[contains(text(),'Add')]").click()
        time.sleep(1)
        # 定位Tenant下拉框并点击
        driver.find_element_by_xpath("(//input[@placeholder='Select'])[1]").click()
        time.sleep(1)
        # 定位Test并点击
        driver.find_element_by_xpath("(//span[contains(text(),'Test')])[1]").click()
        time.sleep(1)
        # 定位Country下拉框并点击
        driver.find_element_by_xpath("(//input[@placeholder='Select'])[2]").click()
        time.sleep(1)
        # 定位Indonesia并点击
        driver.find_element_by_xpath("//span[contains(text(),'Indonesia')]").click()
        time.sleep(1)
        # 定位Legal Entity下拉框并点击
        driver.find_element_by_xpath("(//input[@placeholder='Select'])[3]").click()
        time.sleep(1)
        # 定位TEST000并点击
        driver.find_element_by_xpath("//span[contains(text(),'TEST000')]").click()
        time.sleep(1)
        # 定位Year并选择年份
        driver.find_element_by_xpath("//input[@placeholder='Year']").click()
        time.sleep(1)
        # 定位2020并点击
        driver.find_element_by_xpath("//a[contains(text(),'2020')]").click()
        time.sleep(1)
        # 定位Cycle下拉框并点击
        driver.find_element_by_xpath("(//input[@placeholder='Select'])[4]").click()
        time.sleep(1)
        # 定位CDP Asia Payroll Cycle 并选择
        driver.find_element_by_xpath("//span[contains(text(),'CDP Asia Payroll Cycle')]").click()
        time.sleep(1)
        # 定位Payroll Frequency下拉框并点击
        driver.find_element_by_xpath("(//input[@placeholder='Select'])[5]").click()
        time.sleep(1)
        # 定位Payroll Frequency=1 并点击
        driver.find_element_by_xpath("(//span[contains(text(),'1')])[4]").click()
        time.sleep(1)
        # 定位Generate按钮并点击
        driver.find_element_by_xpath("//span[contains(text(),'Generate')]").click()
        time.sleep(1)
        # 定位Save按钮并点击
        driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()
        time.sleep(1)



        # Cycle Calendar Setup 导入模板
        # 定位Cycle Calendar Setup 并点击
        driver.find_element_by_xpath("//li[contains(text(),'Cycle Calendar Setup')]").click()
        time.sleep(1)
        # 定位Tenant下拉框并点击
        driver.find_element_by_xpath("(//input[@placeholder='Select'])[1]").click()
        time.sleep(1)
        # 定位suez并点击
        driver.find_element_by_xpath("//span[contains(text(),'Suez')]").click()
        time.sleep(1)
        # 定位Add并点击
        driver.find_element_by_xpath("//span[contains(text(),'Add')]").click()
        time.sleep(1)
        # # 定位Import按钮并点击
        # driver.find_element_by_xpath("(//span[contains(text(),'Import')])[2]").send_keys(
        #     "D:\GMS\3_Technical_Documents\GMS Template Documents\Payroll Cycle Calendar Import Template/Cycle.xlsx")
        # time.sleep(2)
        # 定位Save按钮并点击
        driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()
        time.sleep(1)


        # Cycle Calendar Setup 复制
        # 定位Cycle Management并点击
        driver.find_element_by_xpath("//span[contains(text(),'Cycle Management')]").click()
        time.sleep(1)
        # 定位Cycle Calendar Setup 并点击
        driver.find_element_by_xpath("//li[contains(text(),'Cycle Calendar Setup')]").click()
        time.sleep(1)
        #定位Tenant下拉框并点击
        driver.find_element_by_xpath("(//input[@placeholder='Select'])[1]").click()
        time.sleep(1)
        #定位Test 并点击
        driver.find_element_by_xpath("//span[contains(text(),'Test')]").click()
        time.sleep(1)
        # 定位Copy按钮并点击
        driver.find_element_by_xpath("//span[@class='iconfont iconcopy el-tooltip']").click()
        time.sleep(1)
        # 定位Year 并点击
        driver.find_element_by_xpath("(//input[@placeholder='Year'])[2]").click()
        time.sleep(1)
        # 定位2021 并点击
        driver.find_element_by_xpath("//a[contains(text(),'2021')]").click()
        time.sleep(1)
        # 定位Copy按钮并点击
        driver.find_element_by_xpath("(//span[contains(text(),'Copy')])[3]").click()
        time.sleep(1)

        # 新建用户
        # 定位Setup并点击
        driver.find_element_by_xpath("//span[contains(text(),'Setup')]").click()
        time.sleep(1)
        # 定位User List并点击
        driver.find_element_by_xpath("//li[contains(text(),'User List')]").click()
        time.sleep(1)
        # 定位Add并点击
        driver.find_element_by_xpath("//span[contains(text(),'Add')]").click()
        time.sleep(1)
        # User Information页面定位User Name输入框并输入内容
        UserName=driver.find_element_by_xpath("(//input[@class='el-input__inner'])[1]")
        UserName.send_keys("Client.abc")
        time.sleep(1)
        # 定位Role输入框并点击
        driver.find_element_by_xpath("(//input[@placeholder='Select'])[1]").click()
        time.sleep(1)
        # 定位Client HR 并点击
        driver.find_element_by_xpath("//span[contains(text(),'Client HR')]").click()
        time.sleep(1)
        #定位Tenant下拉框并点击
        driver.find_element_by_xpath("(//input[@placeholder='Select'])[2]").click()
        time.sleep(1)
        # 定位租户Test并点击
        driver.find_element_by_xpath("(//span[contains(text(),'Test')])[7]").click()
        time.sleep(1)
        # 定位HR Role下拉框并点击
        driver.find_element_by_xpath("(//input[@placeholder='Select'])[2]").click()
        time.sleep(1)
        #定位Full Access 并点击
        driver.find_element_by_xpath("(//span[contains(text(),'Full Access')])[1]").click()
        time.sleep(1)
        # 定位Payroll Role 下拉框并点击
        driver.find_element_by_xpath("(//input[@placeholder='Select'])[3]").click()
        time.sleep(1)
        # 定位Full Access 并点击
        driver.find_element_by_xpath("(//span[contains(text(),'Full Access')])[1]").click()
        time.sleep(1)
        # 定位Email输入框并点击，+输入内容
        Email=driver.find_element_by_xpath("(//input[@class='el-input__inner'])[5]")
        Email.send_keys("carrie.liu@cdpgroupltd.com")
        time.sleep(1)
        # 定位Admin User 下拉框并点击
        driver.find_element_by_xpath("(//input[@placeholder='Select'])[4]").click()
        time.sleep(1)
        # 定位Admin(Qiang.Zhang@cdpgroupltd.com 并点击
        driver.find_element_by_xpath("//span[contains(text(),'Admin(Qiang.Zhang@cdpgroupltd.com)')]").click()
        time.sleep(1)
        #定位Start Date 并点击
        driver.find_element_by_xpath("(//input[@placeholder='Date'])[1]").click()
        time.sleep(1)
        # 定位日期3号并点击
        driver.find_element_by_xpath("(//span[contains(text(),'3')])[9]").click()
        time.sleep(1)
        # 定位End Date并点击
        driver.find_element_by_xpath("(//input[@placeholder='Date'])[1]").click()
        time.sleep(1)
        # 选择日期2023/1/31
        driver.find_element_by_xpath("(//button[@class='el-picker-panel__icon-btn el-date-picker__next-btn el-icon-d-arrow-right'])[2]").click(3)
        time.sleep(1)
        driver.find_element_by_xpath("(//span[contains(text(),'31')])[4]").click()
        time.sleep(1)
        #定位Custom勾选框并点击
        Custom=driver.find_element_by_xpath("(//span[@class='el-radio__inner'])[2]")
        Custom.send_keys("Abc123")
        time.sleep(1)
        # 定位Save按钮并点击
        driver.find_element_by_xpath("//span[contains(text(),'Save')]").click()
        time.sleep(1)

        pass
