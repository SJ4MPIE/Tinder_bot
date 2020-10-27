from selenium import webdriver
from time import sleep
from secret import email, password
from webdriver_manager.chrome import ChromeDriverManager


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(3)
        login_btn = self.driver.find_element_by_xpath(
            "//*[@id='content']/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button")
        login_btn.click()
        try:
            sleep(1)
            fb_btn = self.driver.find_element_by_xpath(
                "//*[@aria-label='Login with Facebook']")
            fb_btn.click()
        except Exception:
            try:
                sleep(1)
                more_options = self.driver.find_element_by_xpath(
                    '// *[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
                more_options.click()
                sleep(1)
                fb_btn = self.driver.find_element_by_xpath(
                    "//*[@aria-label='Login with Facebook']")
                fb_btn.click()
            except Exception:
                pass

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to.window(base_window)

        accept_cookies = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        accept_cookies.click()
        sleep(5)
        popup_1 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()
        sleep(5)
        popup_2 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath("//*[@aria-label='Like']")
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            "//*[@aria-label='Nope']")
        dislike_btn.click()

    def auto_swipe(self):
        from random import random
        left_count, right_count = 0, 0
        while True:
            sleep(1)
            try:
                rand = random()
                # print(rand)
                if rand < .73:
                    self.like()
                    right_count = right_count + 1
                    print('{}th right swipe'.format(right_count))
                else:
                    self.dislike()
                    left_count = left_count + 1
                    print('{}th left swipe'.format(left_count))
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()
bot.login()
bot.auto_swipe()
# tests
