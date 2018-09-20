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


driver = webdriver.Chrome()  #python
url = driver.command_executor._url       #"http://127.0.0.1:60622/hub"
print(url)
session_id = driver.session_id            #'4e167f26-dc1d-4f51-a207-f761eaf73c31'
driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id
driver.get("http://www.baidu.com")

