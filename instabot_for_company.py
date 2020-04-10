# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 23:19:34 2020

@author: Mecit
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:22:20 2020

@author: Mecit
"""




from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    
    def __init__(self,user_id,user_pass):
        """
        

        Parameters
        ----------
        user_id : TYPE
            DESCRIPTION.
        user_pass : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.user_id=user_id
        self.user_pass=user_pass
        self.driver=webdriver.Chrome('./chromedriver.exe')
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        
    
    def login(self):
        username=self.driver.find_element_by_name('username')
        password=self.driver.find_element_by_name('password')
        username.send_keys(self.user_id)
        password.send_keys(self.user_pass)
        time.sleep(1)
        log_in_button=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div").click()
        time.sleep(4)
        yoksay_button=self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()

    def get_profile(self):
        self.following=[]
        self.followers=[]
        profile=self.driver.get(f'https://www.instagram.com/{self.user_id}')
        time.sleep(0.3)
        open_followers=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(2)
        for a in range(150):
            click_to_box=self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]").click()
            scrool_down=self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN) # scrool_down script
            time.sleep(0.05)
        get_followers=self.driver.find_elements_by_tag_name("a")
        for users in get_followers:
            self.followers.append(users.get_attribute("title"))
        self.filtered_followers=[]
        bos=""
        for non_filtered_users in self.followers:
            if non_filtered_users != bos:
                self.filtered_followers.append(non_filtered_users)
        self.non_followers_dict={}
        for non_followers in self.filtered_followers:
            self.non_followers_dict[non_followers]=(f'https://www.instagram.com/{non_followers}/')    
        print(self.non_followers_dict)
        print(len(self.non_followers_dict))
        
    def unfollow_method(self):
        self.sonradan_kaldirilacak=[]
        self.count=0
        while True:
            for unf_user in self.non_followers_dict:
                self.driver.get(self.non_followers_dict[unf_user])
                time.sleep(0.5)
                unf_button=self.driver.find_element_by_xpath("//button[contains(text(),'Takiptesin')]").click() # "//a[@href'accounts/login']" bunun gibi kullanımı var.
                time.sleep(1.3)                                                                                   # veya "//input[@name='username']"
                unf_agreement=self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
                time.sleep(0.2)
                print(f' user {unf_user} is successfully unfollowed!')
                self.sonradan_kaldirilacak.append(unf_user)
                self.count+=1
                if self.count == 40 or self.count == 40*2 or self.count== 40*3 or self.count == 40*4 or self.count == 40*5:
                    time.sleep(600)
            for removed_user in self.sonradan_kaldirilacak:
                del self.non_followers_dict[removed_user]

us_id=str(input("ID:"))
us_pas=str(input("Pass:"))
print("[+] WARNING YOU WILL UNFOLLOW ALL PEOPLE WITHOUT QUESTIONING.")
mecit=InstagramBot(us_id,us_pas)
mecit.login()
mecit.get_profile()
mecit.unfollow_method()

