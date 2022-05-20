import os
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.common.keys import Keys
import pandas as pd
from numpy import random

# Complete these 2 fields ==================
USERNAME = 'flibyrd.finance'
PASSWORD = 'Ghto12aka'
# ==========================================

TIMEOUT = 6
#LOGIN
# ==========================================
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
mobile_emulation = {
"userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
options.add_experimental_option("mobileEmulation", mobile_emulation)

bot = webdriver.Chrome(executable_path=CM().install(), options=options)
bot.set_window_size(600, 1000)

bot.get('https://www.instagram.com/accounts/login/')

time.sleep(2)

print("[Info] - Logging in...")

user_element = WebDriverWait(bot, TIMEOUT).until(
EC.presence_of_element_located((
    By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/div/label/input')))

user_element.send_keys(USERNAME)

pass_element = WebDriverWait(bot, TIMEOUT).until(
EC.presence_of_element_located((
    By.XPATH, '//*[@id="loginForm"]/div[1]/div[4]/div/label/input')))

pass_element.send_keys(PASSWORD)

login_button = WebDriverWait(bot, TIMEOUT).until(
EC.presence_of_element_located((
    By.XPATH, '//*[@id="loginForm"]/div[1]/div[6]/button')))

time.sleep(0.4)

login_button.click()

time.sleep(15)
# ==========================================




df = pd.read_csv(r'C:\Users\chris\Desktop\InstagramScrape_Flibyrd\scraperFollowers\followers_wallstbets.txt')
usrs = df['username'].tolist()
# ==========================================
sleep1 = random.randint(10)
for usr in usrs:
    print(usr)
    bot.get('https://www.instagram.com/{}/'.format(usr))

    time.sleep(sleep1)

    follow_paths = ['//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button', 
    '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button/div']

    def followProblems():
        try:
            bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div[1]').click()
        except:
            pass
        try:
            bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div[1]/button').click()
        except:
            pass

    success = None
    for btn in follow_paths:
        try:
            bot.find_element_by_xpath(btn).click()
            success = True
        except:
            continue

    sleep2 = random.randint(10)
    if not success:
        followProblems()
        time.sleep(sleep2)

    print('sent follow request')

    message_paths = ['//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div[1]', '//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div[1]/button', 
    '//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div[1]/button/div']

    def messageProblems():
        try:
            bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div[1]').click()
        except:
            pass
        try:
            bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div[1]/button').click()
        except:
            pass
        try:
            bot.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div[1]/button/div').click()
        except:
            pass

    success = None
    for btn in message_paths:
        try:
            bot.find_element_by_xpath(btn).click()
            success = True
        except:
            continue

    if not success:
        sleep3 = random.randint(10)
        messageProblems()
        time.sleep(sleep3)

    print('writing message')

    chat_paths = ['//*[@id="react-root"]/section/div[2]/div/div/div[2]/div/div/div', '//*[@id="react-root"]/section/div[2]/div/div/div[2]/div/div/div/textarea']
    user_message = "Hi there! We're a young start-up with the goal of making investment advice more accessible to everyone. We've developed an app that will replace financial advisors. If you're interested, please sign up for our waitlist! https://flibyrd.com Thank you for your time. " 

    def sendButton():
        try:
            bot.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div/div/div[2]/div/div/div[2]').click()
        except:
            pass
        try:
            bot.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div/div/div[2]/div/div/div[2]/button').click()
        except:
            pass
        try:
            bot.find_element_by_xpath('/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div[2]').click()
        except:
            pass
        try:
            bot.find_element_by_xpath('/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div[2]/button').click()
        except:
            pass

    def chatProblems():
        try:
            l = bot.find_element_by_xpath('/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div')
            l.send_keys(user_message)
            l.send_keys(Keys.RETURN)
            sendButton()
        except:
            pass
        try:
            l = bot.find_element_by_xpath('/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div/textarea')
            l.send_keys(user_message)
            l.send_keys(Keys.RETURN)
            sendButton()
        except:
            pass
    
    sleep4 = random.randint(15)
    time.sleep(sleep4)

    success = None
    for btn in chat_paths:
        try:
            l = bot.find_element_by_xpath(btn)
            l.send_keys(user_message)
            l.send_keys(Keys.RETURN)
            sendButton()
            m = bot.find_element_by_tag_name('textarea')
            m.send_keys(user_message)
            m.send_keys(Keys.RETURN)
            sleep5 = random.randint(10)
            time.sleep(sleep5)
            success = True
        except:
            continue

    if not success:
        sleep5 = random.randint(10)
        chatProblems()
        time.sleep(sleep5)

    print('message sent')
    sleep6 = random.randint(5)
    time.sleep(sleep5)