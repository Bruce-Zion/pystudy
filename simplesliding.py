from selenium.webdriver import ActionChains

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