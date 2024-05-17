import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


account='学号自行填写'
password='密码自己填写'

browser = webdriver.Edge()
browser.get("https://uis.nwpu.edu.cn/cas/login?service=https%3A%2F%2Fecampus.nwpu.edu.cn%2F%3Fpath%3Dhttps%253A%252F%252Fecampus.nwpu.edu.cn%252Fmain.html%2523%252FIndex")
time.sleep(0.3)


logbypass = browser.find_element(by=By.XPATH,value='//*[@id="vue_main"]/div[2]/div[3]/div/div[2]/div[3]/div/div/div[1]/ul/li[3]')
usernameinput = browser.find_element(by=By.ID,value='username')
passwordinput = browser.find_element(by=By.ID,value='password')
login = browser.find_element(by=By.NAME,value='button')

logbypass.click()

usernameinput.send_keys(account)
time.sleep(0.1)
passwordinput.send_keys(password)
time.sleep(0.1)
login.click()
time.sleep(3)
aoxiangjiaowu = browser.find_element(by=By.XPATH,value='/html/body/div/div[1]/div[1]/div/section/div/div[1]/div[2]/div/div[2]/ul[1]/li[4]/span[1]/img')
aoxiangjiaowu.click()


time.sleep(4)

browser.switch_to.window(browser.window_handles[-1])


menu = browser.find_element(by=By.XPATH,value='/html/body/header/nav/div/div[1]/ul[1]/li/a')
ActionChains(browser).move_to_element(menu).perform()
xueji = browser.find_element(by=By.XPATH,value='/html/body/header/nav/div/div[1]/ul[1]/li/div/div[2]/div/div/div/ul/li[3]/a')
ActionChains(browser).move_to_element(xueji).perform()
huaxiang = browser.find_element(by=By.XPATH,value='/html/body/header/nav/div/div[1]/ul[1]/li/div/div[2]/div/div/div/ul/li[3]/div/div[2]/div[1]/a')
huaxiang.click()
time.sleep(8)
content=browser.page_source

with open("gpa.html",'w',encoding='utf-8') as f:
    f.write(content)


