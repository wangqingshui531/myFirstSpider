import urllib.parse
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium import webdriver
import time



def spidermain():
    pages = 'behance_index'
    sleeptime = 10
    timeout = 500
    driver = None
    try:
        #print("start get web %d" % i)
        #driver.refresh()
        driver = webdriver.Firefox()
        start = time.time()
        driver.get('https:\\www.behance.net')
        #loc = (By.ID, 'site-content')
        loc = (By.XPATH, '//*[@id="site-content"]/div[2]/div[2]/div[10]/div/span/a')
        wait = WebDriverWait(driver, timeout)
        list = wait.until(expected_conditions.visibility_of_all_elements_located(loc))
        # WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.ID,"//*[@id='showAlt']"),u'设置'))
        print("111")

        print(str(list[0].get_attribute("href")))
        driver.get(list[0].get_attribute("href"))
        loc = (By.XPATH, '//*[@id="project-modules"]/div/div[1]/div/div/div/img')
        imglist = wait.until(expected_conditions.presence_of_all_elements_located(loc))
        print(driver.title)
        print(str(imglist[2].get_attribute("src")))
        #logger.logspendtime(pages,time.time()-start)
        print("spend time " + str(time.time()-start) + "s")

        try:
            f = open('F:\\Temp\\' + 'first' + ".jpg", 'wb')
            f.write((urllib.request.urlopen(str(imglist[2].get_attribute("src")))).read())
            print('33333')
            f.close()
        except Exception as e:
            print(e)

        driver.quit()
        driver = None
        time.sleep(sleeptime)
    except Exception as err:
        print(err)
        #logger.logspendtime(pages,timeout)
        print("err happend. spend time " + str(timeout) + "s")
        if driver != None:
            driver.quit()
        time.sleep(sleeptime)

spidermain()
#print(str({'word':'hello'}))
#data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding＝'utf8')
#print(str(urllib.parse.urlencode({'word':'hello'})))
#response= urllib.request.urlopen('http://httpbin.org/post’, data=data)
#print(response.read())


#request = urllib.request.Request('https://www.behance.net')
#response = urllib.request.urlopen(request)
#print(response.read().decode('utf-8'))
#print(response.read().decode('utf-8'))
#print(response.read().decode('utf-8'))