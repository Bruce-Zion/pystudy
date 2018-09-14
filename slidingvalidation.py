from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import shutil
from PIL import Image
import time


def get_snap(driver):
    driver.save_screenshot('full_snap.png')
    page_snap_obj = Image.open('full_snap.png')

    return page_snap_obj


def get_image(driver):
    img = driver.find_element_by_class_name('geetest_canvas_img')
    time.sleep(2)
    location = img.location
    size = img.size

    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']

    page_snap_obj = get_snap(driver)

    image_obj = page_snap_obj.crop((left, top, right, bottom))
    # image_obj.show()
    with open('code.png', 'wb') as f:
        image_obj.save(f, format='png')
    return image_obj


def get_distance(image1, image2):
    # start = 0
    # threhold = 70
    # for i in range(start, image1.size[0]):
    #     for j in range(0, image1.size[1]):
    #         rgb1 = image1.load()[i, j]
    #         rgb2 = image2.load()[i, j]
    #         res1 = abs(rgb1[0] - rgb2[0])
    #         res2 = abs(rgb1[1] - rgb2[1])
    #         res3 = abs(rgb1[2] - rgb2[2])
    #         # print(res1,res2,res3)
    #         if not (res1 < threhold and res2 < threhold and res3 < threhold):
    #             print(111111, i, j)
    #             return i - 13
    # print(2222, i, j)
    # return i - 13
    start = 0
    threhold = 70
    v = []
    for i in range(start, image1.size[0]):
        for j in range(0, image1.size[1]):
            rgb1 = image1.load()[i, j]
            rgb2 = image2.load()[i, j]
            res1 = abs(rgb1[0] - rgb2[0])
            res2 = abs(rgb1[1] - rgb2[1])
            res3 = abs(rgb1[2] - rgb2[2])

            if not (res1 < threhold and res2 < threhold and res3 < threhold):
                print(i)
                if i not in v:
                    v.append(i)

    stop = 0
    for i in range(0, len(v)):
        val = i + v[0]
        if v[i] != val:
            stop = v[i]
            break

    width = stop - v[0]
    print(stop, v[0], width)
    return width


def get_tracks(distance):
    import random
    exceed_distance = random.randint(0, 5)
    distance += exceed_distance  # 先滑过一点，最后再反着滑动回来
    v = 0
    t = 0.2
    forward_tracks = []

    current = 0
    mid = distance * 3 / 5
    while current < distance:
        if current < mid:
            a = random.randint(1, 3)
        else:
            a = random.randint(1, 3)
            a = -a
        s = v * t + 0.5 * a * (t ** 2)
        v = v + a * t
        current += s
        forward_tracks.append(round(s))

    # 反着滑动到准确位置
    v = 0
    t = 0.2
    back_tracks = []

    current = 0
    mid = distance * 4 / 5
    while abs(current) < exceed_distance:
        if current < mid:
            a = random.randint(1, 3)
        else:
            a = random.randint(-3, -5)
            a = -a
        s = -v * t - 0.5 * a * (t ** 2)
        v = v + a * t
        current += s
        back_tracks.append(round(s))
    return {'forward_tracks': forward_tracks, 'back_tracks': list(reversed(back_tracks))}


def crack(driver):  # 破解滑动认证
    # 1、点击按钮，得到没有缺口的图片
    button = driver.find_element_by_xpath('//*[@id="embed-captcha"]/div/div[2]/div[1]/div[3]')
    button.click()

    # 2、获取没有缺口的图片
    image1 = get_image(driver)

    # 3、点击滑动按钮，得到有缺口的图片
    button = driver.find_element_by_class_name('geetest_slider_button')
    button.click()

    # 4、获取有缺口的图片
    image2 = get_image(driver)

    # 5、对比两种图片的像素点，找出位移
    distance = get_distance(image1, image2)
    print(distance)
    #
    # 6、模拟人的行为习惯，根据总位移得到行为轨迹
    tracks = get_tracks(int(distance / 2))

    # 7、按照行动轨迹先正向滑动，后反滑动
    button = driver.find_element_by_class_name('geetest_slider_button')
    ActionChains(driver).click_and_hold(button).perform()

    # 正常人类总是自信满满地开始正向滑动，自信地表现是疯狂加速
    for track in tracks['forward_tracks']:
        ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()

    # 结果傻逼了，正常的人类停顿了一下，回过神来发现，卧槽，滑过了,然后开始反向滑动
    time.sleep(0.5)
    for back_track in tracks['back_tracks']:
        ActionChains(driver).move_by_offset(xoffset=back_track, yoffset=0).perform()
    #
    # # 小范围震荡一下，进一步迷惑极验后台，这一步可以极大地提高成功率
    ActionChains(driver).move_by_offset(xoffset=3, yoffset=0).perform()
    ActionChains(driver).move_by_offset(xoffset=-3, yoffset=0).perform()

    # # 成功后，骚包人类总喜欢默默地欣赏一下自己拼图的成果，然后恋恋不舍地松开那只脏手
    time.sleep(0.5)
    ActionChains(driver).release().perform()


def login_luffy(username, password):
    driver = webdriver.Chrome()
    driver.set_window_size(960, 800)
    try:
        # 1、输入账号密码回车
        driver.implicitly_wait(3)
        driver.get('https://www.luffycity.com/login')
        input_username = driver.find_element_by_xpath('//*[@id="router-view"]/div/div/div[2]/div[2]/input[1]')
        input_pwd = driver.find_element_by_xpath('//*[@id="router-view"]/div/div/div[2]/div[2]/input[2]')

        input_username.send_keys(username)
        input_pwd.send_keys(password)

        # 2、破解滑动认证
        crack(driver)

        time.sleep(10)  # 睡时间长一点，确定登录成功
    finally:
        pass
        # driver.close()


if __name__ == '__main__':
    login_luffy(username='wupeiqi', password='123123123')


#https://blog.csdn.net/jingjing_94/article/details/80555511
#https://blog.csdn.net/u012067766/article/details/79793264
