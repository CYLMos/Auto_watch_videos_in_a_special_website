import sys
import selenium.webdriver as webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep

account = str(sys.argv[1])
password = str(sys.argv[2])

browser = webdriver.Chrome()
browser.get('http://www.course.acad.nsysu.edu.tw/TAsystem/login.php')
element = browser.find_element_by_id("fancybox-close")
element.click()

account_element = browser.find_element_by_name('id')
password_element = browser.find_element_by_name('password')

# Enter account
account_element.clear
account_element.send_keys(account)

# Enter password
password_element.clear
password_element.send_keys(password)

# Click the login button
login_element = browser.find_element_by_xpath("//input[@value='登入Login']")
login_element.click()

# Wait alert
sleep(3)
# Accept the alert
browser.switch_to.alert.accept()

# Go to the video page
video_link_element = browser.find_element_by_xpath("//a[@href='stu_class_list.php']")
video_link_element.click()

# Wait alert
sleep(3)
# Accept the alert
browser.switch_to.alert.accept()

video_link_id_list = ['ta001', 'ta002', 'ta003', 'ta004']
time_list = [3600, 5400, 5400, 5400]
wait_alert_time = 600

for i in range(0, 4, 1):
    iframe_element = browser.find_element_by_name('mainFrame')
    browser.switch_to_frame(iframe_element)

    video_link_element = browser.find_element_by_id(video_link_id_list[i])
    video_link_element.click()

    sleep(1)

    # Switch to the youtube iframe
    iframe_yt_element = browser.find_element_by_xpath("//iframe[@width='560']")
    browser.switch_to_frame(iframe_yt_element)

    # Click the play button
    video_play_element = browser.find_element_by_xpath("//button[@class='ytp-large-play-button ytp-button']")
    video_play_element.click()

    for j in range(time_list[i], 0, -wait_alert_time):
        print(j)
        # Wait ten minutes
        sleep(wait_alert_time)

        # Handle the alert
        try:
            sleep(3)
            browser.switch_to.alert.accept()
        except TimeoutException as e:
            sleep(10)
            browser.switch_to.alert.accept()
    # Out the youtube iframe
    browser.switch_to.parent_frame()
    # To default content
    browser.switch_to.default_content()

    # Go to the video page 
    video_link_element = browser.find_element_by_xpath("//a[@href='stu_class_list.php']")
    video_link_element.click()

    # Wait alert
    sleep(3)
    # Accept the alert
    browser.switch_to.alert.accept()

browser.close()

