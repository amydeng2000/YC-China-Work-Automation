from selenium import webdriver
import pandas as pd
import requests

browser = webdriver.Chrome()

browser.get("https://www.aminer.cn/")
browser.find_element_by_xpath('//*[@id="root"]/section/div[1]/div/header/div[2]/ul/li[3]').click()
browser.find_element_by_xpath('//*[@id="userPhone"]').send_keys("15611947467")
browser.find_element_by_xpath('//*[@id="phonePassword"]').send_keys("Xyyyhtl0")
browser.find_element_by_xpath('//*[@id="root"]/section/main/main/article/section/div/div[1]/div[3]/div[1]/form/div/div[5]/div/div/span/button').click()

data = pd.read_csv("aminer.csv")
profile_ids = data['id']

for i in range(len(profile_ids)):
    profile_id = profile_ids[i]
    url = 'https://www.aminer.cn/profile/{0}'.format(profile_id)
    browser.get(url)

    for j in range(3):
        try:
            image_link = browser.find_element_by_css_selector(".email.info_line").find_element_by_tag_name("img").get_attribute("src")
            r = requests.get(image_link)
            with open("./emails/{0}.png".format(profile_id), "wb") as f:
                f.write(r.content)
            print("{0}/{1} {2} saved".format(i, len(profile_ids), profile_id))
            break
        except:
            browser.refresh()
