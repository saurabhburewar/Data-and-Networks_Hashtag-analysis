import pandas as pd
import time
import os
import pickle
from datetime import date, datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def find_element_safe(self, by, className):
    try:
        return self.find_element(by, className)
    except NoSuchElementException:
        return None


def scrap():
    data = pd.DataFrame(
        columns=['username', 'date', 'content', 'likes', 'hashtags', 'rekoo_users'])

    # feed = driver.find_element(
    #     By.XPATH, '//*[@id="scrollContainer"]/div/div[2]/div/div/div')
    feedList = driver.find_elements(
        By.XPATH, '//*[@id="scrollContainer"]/div/div[2]/div/div/div/*')

    for post in feedList:
        # rekoo_users_url = []
        rekoo_users = []
        hashtags = []

        if post.get_attribute('class') != '_2nxUQ':
            if post.get_attribute('id') not in parsed:
                profile_name = post.find_element(By.CLASS_NAME, 'tvkyd').text
                # profile_url = post.find_element(
                #     By.CLASS_NAME, 'tvkyd').get_attribute('href')
                stamp = post.find_element(By.CLASS_NAME, '_3AAWv').text
                username = post.find_element(By.CLASS_NAME, 'xJqZd').text

                if ' ' in stamp:
                    if len(stamp.split(' ')) == 3:
                        post_time = datetime.strptime(stamp, "%d %b %Y")
                        post_time = post_time.strftime()
                    elif len(stamp.split(' ')) == 2:
                        post_time = datetime.strptime(
                            stamp+' '+str(date.today().year), "%d %b %Y")
                        post_time = post_time.strftime('%d-%m-%Y')
                else:
                    curr_date = date.today()
                    if 'd' in stamp:
                        post_time = curr_date - timedelta(days=int(stamp[0]))
                    elif 'h' in stamp:
                        post_time = curr_date
                    elif 'm' in stamp:
                        post_time = curr_date

                post_content = post.find_element(By.CLASS_NAME, '_3NfMI')
                post_text = post_content.text
                for tag in post_content.find_elements(By.TAG_NAME, 'a'):
                    if "#" in tag.text:
                        hashtags.append(tag.text)

                bottom_bar = post.find_element(By.CLASS_NAME, '_3DO8S')
                for index, bottom_opts in enumerate(bottom_bar.find_elements(By.CLASS_NAME, '_1dSco')):
                    if index == 1:
                        continue
                    elif index == 0:
                        if find_element_safe(bottom_opts, By.CLASS_NAME, '_3Y7lQ') is None:
                            likes = None
                        else:
                            likes = bottom_opts.find_element(
                                By.CLASS_NAME, '_3Y7lQ').text

                    elif index == 2:
                        if find_element_safe(bottom_opts, By.CLASS_NAME, '_3Y7lQ') is None:
                            # rekoo_users_url = None
                            rekoo_users = None
                        else:
                            rekoo_but = bottom_opts.find_element(
                                By.CLASS_NAME, '_3Y7lQ')
                            rekoo_num = rekoo_but.text
                            rekoo_but.click()
                            time.sleep(5)
                            modal = driver.find_element(
                                By.CLASS_NAME, 'modal-content')
                            modal_list = modal.find_element(
                                By.CLASS_NAME, 'list-group').find_elements(By.TAG_NAME, 'a')

                            for user in modal_list:
                                # rekoo_users_url.append(
                                #     user.get_attribute('href'))
                                rekoo_users.append(user.find_element(
                                    By.CLASS_NAME, '_2QZUb').text)

                            modal.find_element(By.CLASS_NAME, 'close').click()

                    elif index == 3 or index == 4:
                        break

                ith_post = [username, post_time, post_text,
                            likes, hashtags, rekoo_users]
                data.loc[len(data)] = ith_post
                parsed.append(post.get_attribute('id'))

    print("Posts parsed: ", len(parsed))
    data.to_csv('covid_data.csv', mode='a')

    with open('parsed_ids.txt', 'ab') as fp:
        pickle.dump(parsed, fp)


options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)

driver.get('https://www.kooapp.com/tag/covid19')

time.sleep(5)
driver.execute_script("document.body.scrollTo(0, document.body.scrollHeight)")
container = driver.find_element(By.ID, 'scrollContainer')

if os.path.isfile('parsed_ids.txt'):
    with open('parsed_ids.txt', 'rb') as fp:
        parsed = pickle.load(fp)
else:
    parsed = []

scroll_count = 0

while True:

    scrap()

    old_height = driver.execute_script(
        "return document.getElementById('scrollContainer').scrollHeight;")
    driver.execute_script(
        "document.getElementById('scrollContainer').scrollTo({top: document.getElementById('scrollContainer').scrollHeight, left: 0, behavior: 'smooth'});")
    time.sleep(5)
    if scroll_count == 0:
        driver.maximize_window()
        time.sleep(5)

    new_height = driver.execute_script(
        "return document.getElementById('scrollContainer').scrollHeight;")

    scroll_count += 1

    if new_height == old_height:
        break

    # if scroll_count == 2:
    #     break
