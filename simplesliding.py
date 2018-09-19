from selenium import webdriver
from selenium.webdriver import ActionChains

# Configure the necessary command-line option.
options = webdriver.ChromeOptions()
options.add_argument(r'--load-extension=C:\Users\mtk81153\AppData\Local\Google\Chrome\User Data\Profile 2\Extensions\ammjpmhgckkpcamddpolhchgomcojkle\6.1.10_0')

# Initalize the driver with the appropriate options.
driver = webdriver.Chrome(chrome_options=options)


action = ActionChains(driver)

source=driver.find_element_by_xpath("//*[@id='nc_1_n1t']/span")#需要滑动的元素
action.click_and_hold(source).perform()  #鼠标左键按下不放
action.move_by_offset(298,0)#需要滑动的坐标
action.release().perform() #释放鼠标
time.sleep(0.1)


#判断弹框是否弹出
#https://www.cnblogs.com/yoyoketang/p/6569170.html
from selenium.webdriver.support import expected_conditions as EC

result = EC.alert_is_present()(driver)
if result:
    print result.text
    result.accept()
else:
    print "alert 未弹出！"


#https://blog.csdn.net/xiaosongbk/article/details/53262796
#Selenium Webdriver弹出框的种种类型

#https://troubleshootblog.com/2014/11/06/code-automating-extension-automation-with-selenium/
Code : Automating Extension automation with Selenium
Below code is for Chrome. This will work for Firefox  with little change in code.

// Load extension file
File file = new File(“chrome.crx”);
ChromeOptions options = new ChromeOptions();
options.addExtensions(file);

// Launch browser instance with the extension
WebDriver driver = new ChromeDriver(options);

// Access Extension in browser window .. This further allows you to automate all the actions through Selenium
driver.get(“extension://palgcoflnoaklkflllnmheiollkgkipm/popup.html”);

#https://huddle.eurostarsoftwaretesting.com/how-to-selenium-popups-with-selenium/
#http://www.cnblogs.com/xingkongyihao/p/9280983.html
#https://www.cnblogs.com/small-bud/p/9064485.html