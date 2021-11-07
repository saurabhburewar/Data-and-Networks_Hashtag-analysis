import pandas as pd
import time
from datetime import date, datetime, timedelta
from selenium import webdriver
from bs4 import BeautifulSoup


def scrap():
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    feed = soup.find('div', class_='infinite-scroll-component')
    count = 0

    data = pd.DataFrame(columns=['profile_name', 'profile_url', 'username', 'activity',
                                 'post_time', 'post_text', 'post_img', 'post_poll_votes', 'likes', 'hashtags'])

    for post in feed.findChildren('div', recursive=False):
        if count != 0:
            hashtags = []
            # activity = number of posts when this post was posted
            activity = post.find('div', class_='_3BeHF').text
            name_time = post.find('div', class_='nameAndTimeStamp')
            name_time_a = name_time.find('a', class_='tvkyd', href=True)
            profile_name = name_time_a.text
            profile_url = 'https://www.kooapp.com{}'.format(
                name_time_a['href'])

            stamp = name_time.find('div', class_='_3AAWv').text
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

            username = post.find('a', class_='xJqZd').text

            post_content = post.find('span', class_='_3NfMI')
            post_text = post_content.text
            for tag in post_content.find_all('a'):
                if '#' in tag.text:
                    hashtags.append(tag.text)

            if post.find('div', class_='_2-IMR') is None:
                post_img = None
            else:
                post_img = post.find('div', class_='_2-IMR').find('img')['src']

            post_poll_box = post.find('div', class_='_2V3dL')

            if post_poll_box is None:
                post_poll = None
                post_poll_votes = None
            else:
                post_poll_votes = post_poll_box.find(
                    'span', class_='MH91b').find('p').text

            bottom_bar = post.find('div', class_='_3DO8S')
            if bottom_bar.find('div', class_='_3Y7lQ') is None:
                likes = 0
            else:
                likes = bottom_bar.find('div', class_='_3Y7lQ').text

            ith_post = [profile_name, profile_url, username, activity,
                        post_time, post_text, post_img, post_poll_votes, likes, hashtags]

            data.loc[len(data)] = ith_post

        count += 1

    print(count)
    data.to_csv('koo_VaccineCentury.csv')


options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.kooapp.com/tag/VaccineCentury')

time.sleep(5)
driver.execute_script("document.body.scrollTo(0, document.body.scrollHeight)")
feed = driver.find_element_by_id('scrollContainer')

scroll_count = 0
print("Waiting for the page to load...")

while True:
    old_height = driver.execute_script(
        "return document.getElementById('scrollContainer').scrollHeight;")
    driver.execute_script(
        "document.getElementById('scrollContainer').scrollTo({top: document.getElementById('scrollContainer').scrollHeight, left: 0, behavior: 'smooth'});")
    time.sleep(2)
    if scroll_count == 0:
        driver.maximize_window()
        time.sleep(2)
    # driver.execute_script(
    #     "document.getElementById('scrollContainer').scrollTo({top: -50, left: 0, behavior: 'smooth'});")
    # time.sleep(10)
    new_height = driver.execute_script(
        "return document.getElementById('scrollContainer').scrollHeight;")

    print("Scroll Count: ", scroll_count)
    scroll_count += 1

    if new_height == old_height:
        break

    # if scroll_count == 5:
        #     break


time.sleep(2)
scrap()
