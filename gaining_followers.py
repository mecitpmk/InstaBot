# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 05:09:48 2020

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
        user_id : str
            user id 
        user_pass : str
            user password

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
        

    def get_hashtag(self,hashtag_name):
        self.driver.get(f'https://www.instagram.com/explore/tags/{hashtag_name}/')
        time.sleep(1)
        for a in range(900):
            scrool_down=self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_DOWN) # scrool_down script
        tag_name=self.driver.find_elements_by_tag_name('a')
        self.photos_list=[elem.get_attribute('href') for elem in tag_name]
        self.photos_list=[links for links in self.photos_list]
        self.filtered_links=[]
        specified="https://www.instagram.com/p/" # 27 index has
        test_count=0
        for link in self.photos_list:
            if link[0:28] == specified:
                self.filtered_links.append(link)
            else:
                test_count+=1
                print("not included pictures link",test_count)
        for get_link in self.filtered_links:
            self.driver.get(get_link)
            time.sleep(1)
            like_button=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/article/div[2]/section[1]/span[1]/button").click()
            time.sleep(0.5)

enter_id=str(input("Instagram ID:"))
enter_pass=str(input("Instagram Passw:"))
which_hashtag=str(input("Hashtag ( Başına # KOYMAYINIZ ! ):"))


mecit=InstagramBot(enter_id,enter_pass)
mecit.login()
mecit.get_hashtag(which_hashtag)
