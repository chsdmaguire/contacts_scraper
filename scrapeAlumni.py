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
from html import unescape
import unicodedata
import re


years = ['2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004']

for item in years:
    URL = 'https://mysantaclara.scu.edu/directory/logout?bm=145108421'
    # Complete these 2 fields ==================
    USERNAME = 'cmaguire'
    PASSWORD = 'P@sswordCHR1S'
    # ==========================================

    CLASSYEAR = item
    TIMEOUT = 1
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
    bot.set_window_size(1000, 1000)

    bot.get(URL)
    time.sleep(2)
    print("[Info] - Logging in...")

    user_element = WebDriverWait(bot, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH, '//*[@id="PC2820_txtUsername"]')))

    user_element.send_keys(USERNAME)

    pass_element = WebDriverWait(bot, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH, '//*[@id="PC2820_txtPassword"]')))

    pass_element.send_keys(PASSWORD)

    login_button = WebDriverWait(bot, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH, '//*[@id="PC2820_btnLogin"]')))

    time.sleep(0.4)

    login_button.click()

    #ALUMNI SEARCH
    # ==========================================
    search_link = WebDriverWait(bot, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH, '//*[@id="content"]/div/div[2]/nav/ul/li[2]/a')))

    time.sleep(0.4)

    search_link.click()

    class_input = WebDriverWait(bot, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH, '//*[@id="PC2825_52_0"]')))
    class_input.send_keys(CLASSYEAR)
    time.sleep(0.4)

    alumSearch_button = WebDriverWait(bot, TIMEOUT).until(
            EC.presence_of_element_located((
                By.XPATH, '//*[@id="PC2825_btnRefresh"]')))
    alumSearch_button.click()
    time.sleep(0.4)
    #ITERATE OVER ALUMNI
    # ==========================================
    def getUrls():
        table_class = bot.find_element_by_xpath('//*[@id="PC2825_directoryOutputGridView_myGridView"]')
        rows = table_class.find_elements_by_tag_name('tr')
        studentLinks = []
        for row in rows:
            try:
                name_link = row.find_element_by_tag_name('a')
                lnk = name_link.get_attribute('onclick')
                studentLinks.append(lnk)
            except:
                pass   
        time.sleep(.5)
        studentLinks.remove(None)
        return studentLinks

    arrOfLinks = []
    for i in range(7):
        try:
            item = getUrls()
            arrOfLinks += item
            next_button = bot.find_element_by_class_name('BBPagerNextPageLink')
            next_button.click()
            time.sleep(1)
        except:
            pass

    print(arrOfLinks)
    # ==========================================
    time.sleep(1)
    def checkText(item, arr):
        checker = True
        for i in arr:
            if(i == item):
                checker = False
        return checker

    CLEANR = re.compile('<.*?>') 

    bad_items = ['Personal Information', 'Name:', '',  'Preferred SCU Class of:', 
    'Nickname:', 'Last Name while at SCU:', '', '', 'Gender:', 
    'Marital Status:', '', 'Unknown', 'Contact Information', 'Address:', '', 
    'Home Phone:', '', '', 'Business Phone:', '', '', 'Primary Email:', '', 'Spouse/Partner', "My Spouse/Partner's Name:", '', '', 'Name While at SCU (If Alumni):', '', '', 'SCU Class of:', '', '', 'Professional Information', 'Business Name:', '', '', 'Position:', '', '', 'Business Address:', '', 
    '', 'Willing to Network:', '', '', 'SCU Education', 'Preferred Class of:', '', 'School:', 'Degree:']

    allStudents = []
    print('--------------------------------------------------------------------')
    print('GETTING CONTACT DATA')
    for url in arrOfLinks:
        if(url != None):
            try:
                bot.get(url)
                time.sleep(.2)
                student_table = bot.find_element_by_tag_name('table')
                info = student_table.find_elements_by_tag_name('td')
                student_arr = []
                for item in info:
                    try:
                        raw_text = item.get_attribute('innerHTML')
                        cleantext = re.sub(CLEANR, '', raw_text)
                        s = unescape(cleantext)
                        s = unicodedata.normalize('NFKC', s)
                        s = s.strip()
                        cleanUp = checkText(s, bad_items)
                        if(cleanUp):
                            student_arr.append(s)
                    except:
                        pass
                print(student_arr)
                allStudents.append(student_arr)

            except:
                pass

    print('--------------------------------------------------------------------')
    print('finished gathering student data')

    with open('studentData{}.txt'.format(CLASSYEAR), "w") as f:
        for item in allStudents:
            try:
                f.write(' '.join(item) + '\n')
            except:
                pass