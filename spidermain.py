import urllib.parse
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os
import mylog
import details
import urllib

targetdir='G:\\behance'
logger=mylog.log()
detailmgr=details.detailmgr()
sleeptime=10
timeout=180

def save_img(src,targetdir):
    #保存图片到磁盘文件夹 targetdir，默认为当前脚本运行目录下的 book\img文件夹
    try:
        targetfilename=os.path.basename("/" + src)
        if not os.path.exists(targetdir):
            print('targetdir no exists  :'+ targetdir)
            logger.logruninfo(targetdir + ' not exists, create it')
            os.makedirs(targetdir)
            print("mkdir " + targetdir)
        targetpath = targetdir + '\\' + targetfilename
        urllib.request.urlretrieve(src,filename=targetpath)
        logger.logruninfo(src + ' copy to ' + targetpath)
    except IOError as e:
        print("IOERROR")
        print(e)
    except Exception as e:
        print("Exception")
        print(e)

def spidermain():
    pages = 'behance_index'
    sleeptime = 10
    timeout = 120
    driver = None
    try:
        #print("start get web %d" % i)
        #driver.refresh()
        driver = webdriver.Firefox()
        start = time.time()
        driver.get('https:\\www.behance.net')
        #loc = (By.ID, 'site-content')
        loc = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/span/a')
        wait = WebDriverWait(driver, timeout)
        list = wait.until(expected_conditions.visibility_of_all_elements_located(loc))
        # WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.ID,"//*[@id='showAlt']"),u'设置'))
        print("111===========" + str(len(list)))
        i = 1;
        time.sleep(30)
        hreflist=[]
        for element in list:
            href = element.get_attribute("href")
            print(href)
            hreflist.append(href)
        driver.quit()
        time.sleep(30)

        for detailpageurl in hreflist:
            print(str(i) +" detail "+ detailpageurl)
            if detailmgr.isDownloaded(detailpageurl):
                print(detailpageurl + " even is downloaded,no more")
                continue
            #根据明细URL获取一个目录名称，保存明细URL内的所有图片
            subdirname = detailpageurl.split('/')[5].split('?')[0]

            try:
                driver = webdriver.Firefox()
                driver.get(detailpageurl)
                logger.logruninfo("GET :" + detailpageurl)
                time.sleep(20)
                loc = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/a[2]')
                wait = WebDriverWait(driver, timeout)
                wait.until(expected_conditions.visibility_of_element_located(loc))
                print("wait util svg ok....")
                imglist = []
                imglist = driver.find_elements_by_xpath('//img')
                print("how many pic : " + str(len(imglist)))
                logger.logruninfo("wait until :" + detailpageurl + " " + str(len(imglist)))
                time.sleep(10)
                srclist=[]
                for imgelement in imglist:
                    src = imgelement.get_attribute("src")
                    logger.logruninfo('src: ' + src)
                    srclist.append(src)
                driver.quit()
                driver = None
                for src in srclist:
                    start = time.time()
                    save_img(src, targetdir + "\\" + subdirname)
                    time.sleep(1)
                    print("spend time " + str(time.time() - start) + "s")
                detailmgr.adddetails(detailpageurl)

                #国外网站需要慢速下载，否则报错
                time.sleep(60)
                i = i + 1
            except Exception as e:
                print(e)
                print("Exception9121")
                if driver != None:
                    driver.quit()
                time.sleep(150)
                logger.logruninfo(str(e))

    except Exception as err:
        print(err)
        print("Exception98820")
        logger.logruninfo(err)
        #logger.logspendtime(pages,timeout)
        print("err happend. spend time " + str(timeout) + "s")
        if driver != None:
            driver.quit()

for i in range(10):
    spidermain()
    time.sleep(300)

#import urllib.request
#response= urllib.request.urlopen('https://www.behance.net/gallery/75632903/Drapery?tracking_source=best_of_behance')
#print(response.read().decode('utf-8'))

