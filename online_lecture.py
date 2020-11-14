from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
# from secret import pw1
from selenium.webdriver.chrome.options import Options
import pyfiglet
import datetime

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })



def sendkeys(driver, element, timeout, value):
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located(element)).send_keys(value)

def click(driver, element, timeout):
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(element)).click()    

def login():
    driver.maximize_window()
    gmail = "enter your own email id"
    pw1 = "Enter your password"
    main_page = driver.get('https://accounts.google.com/')
    email = (By.XPATH, '//input[@type="email"]')
    sendkeys(driver, email, 20, gmail)
    Next = (By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc']")
    click(driver, Next, 20)
    sleep(4)
    password = (By.XPATH, "//input[@type='password']")
    sendkeys(driver, password, 20, pw1)
    Next = (By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc']")
    click(driver, Next, 20)
    sleep(2)

def lecture():
    driver.get('https://meet.google.com/zbo-hxdj-cou')
    sleep(2)

def practical():
    driver.get('https://meet.google.com/ygw-gocn-snm')

def micro():
    mic = (By.XPATH, '//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[1]/div/div/div')
    try:
        click(driver, mic, 20)
    except Exception:
        micro()
    sleep(2)

def video():
    Video_off = (By.XPATH, '//*[@id="ow3"]/div[1]/div/div[5]/div[3]/div[9]/div[2]/div[3]/div/div')
    try:
        click(driver, Video_off, 20)
    except Exception:
        video()
    sleep(2)

def join():
    Join_Now = (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]')
    try:
        click(driver, Join_Now, 20)
    except Exception:
        join()
    sleep(5)
    
check = True
flag = False
loginn = True

if __name__ == "__main__":
    intro = pyfiglet.figlet_format("Codegrammed", font="slant")
    print(intro + "\n")
    intro = pyfiglet.figlet_format("BOT TO ATTEND ONLINE LECTURES", font="digital")
    print(intro)

    while True:
        date = datetime.date.today()
        time = datetime.datetime.now().ctime()
        curr_date_time = time.split()
        Day, Month, Date, Time, Year = curr_date_time[0], curr_date_time[1], curr_date_time[2], curr_date_time[3], curr_date_time[4]
        time = Time.split(":")
        hour, mins, sec = time[0], time[1], time[2]
        hour_min = hour + mins

        if Day != "Sun":
            if hour_min >= "0900" and hour_min <= "1230" :
                if check:
                    print("Online Lectures")
                    driver = webdriver.Chrome(chrome_options=opt,service_log_path='NUL')
                    login()
                    lecture()
                    join()
                    micro()
                    check = False
                    flag = True

            elif hour_min >= "1320" and hour_min <= "1540" :
                if check:
                    print("Online Practicals")
                    driver = webdriver.Chrome(chrome_options=opt,service_log_path='NUL')
                    login()
                    practical()
                    join()
                    micro()
                    check = False
                    flag = True
            
            else:
                if flag:
                    End = (By.XPATH, '//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[2]/div')
                    click(driver, End, 20)
                    flag = False
                    check = True
                    driver.close()
                
                if hour_min >='1541' :
                    if loginn:
                        driver.close()
                        loginn = False
