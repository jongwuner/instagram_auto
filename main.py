from selenium import webdriver
import time
import random

from selenium.common.exceptions import NoSuchElementException


def login(driver) :
    id_form = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    id_form.send_keys('id')
    pw_form = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    pw_form.send_keys('pw')
    pw_form.submit()
    time.sleep(5)

def work(driver) :
    i = 1
    while True :
        try :
            while True :
                hashtag = "좋아요반사"
                driver.get("https://www.instagram.com/explore/tags/" + hashtag)
                time.sleep(random.randint(5, 8))
                picture = driver.find_elements_by_class_name('_9AhH0')[9]
                picture.click()
                time.sleep(random.randint(10, 30))
                try:
                    like_btn = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
                    like_btn.click()
                except:
                    time.sleep(10)
                time.sleep(random.randint(5, 7))
                print("%d 번째 실행" % i)
                i += 1
        except NoSuchElementException as e:
            print("[Error] ", e)
            pass
        except Exception as e:
            print("[Error] 주기값을 조정 필요합니다", e.args)
def main() :
    driver = webdriver.Chrome(r'chromedriver.exe')
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(5)

    login(driver)
    work(driver)

main()
