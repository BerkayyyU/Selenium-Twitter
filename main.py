from re import T
from attr import asdict
from selenium import webdriver
from time import sleep
import users
import links
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Bot():
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.login(users.user['username'],users.user['password'])
        for tweet in links.tweets:
            self.navigateToLink(tweet)
            self.like()
            self.retweet()
            self.reply(users.user_reply_text)  
            
        self.logout()   
        sleep(1000)


    def login(self, username, password):
        self.driver.get(links.login_link)
        sleep(2)

        username_input = self.findElementByXPath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        username_input.send_keys(username)
        sleep(1)
        username_input.send_keys(Keys.ENTER)
        sleep(3)

        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)
        sleep(1)
        password_input.send_keys(Keys.ENTER)
        sleep(3)

    def logout(self):
        profile_icon = self.findElementByXPath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[2]')
        profile_icon.click()
        sleep(1)

        logout_text = self.findElementByXPath('//a[@href="'+'/logout'+'"]')
        logout_text.click()
        sleep(1)

        logout_btn = self.findElementByXPath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]')
        logout_btn.click()
        sleep(2)

    def navigateToLink(self,link):
        self.driver.get(link)
        sleep(2)

    def like(self):
        likeEl = self.findElementByXPath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div[1]/article/div/div/div/div[3]/div[5]/div/div[3]')
        likeEl.click()
        sleep(1)
    
    def retweet(self):
        retweetDialog = self.findElementByXPath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div[1]/article/div/div/div/div[3]/div[5]/div/div[2]')
        retweetDialog.click()
        sleep(1)

        retweetEl = self.findElementByXPath('//*[@id="layers"]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div')
        retweetEl.click()
        sleep(1)

    def reply(self, text):
        reply_text = self.driver.find_element(By.CSS_SELECTOR, "[aria-label='Tweet text']")
        
        sleep(1)
        reply_text.send_keys(text)
        sleep(1)

        reply_btn = self.findElementByXPath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]')
        reply_btn.click()
        sleep(3)


    def findElementByXPath(self,xpath):
        return self.driver.find_element(By.XPATH,xpath)

def main():
    my_bot = Bot()

if __name__ == '__main__':
    main()