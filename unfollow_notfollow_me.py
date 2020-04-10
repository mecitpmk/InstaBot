# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 20:22:20 2020

@author: Mecit
"""




from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
from selenium.webdriver.common.touch_actions import TouchActions
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
        self.driver=webdriver.Chrome('C:/Users/Mecit/chromedriver.exe')
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        
    def login(self):
        username=self.driver.find_element_by_name('username')
        password=self.driver.find_element_by_name('password')
        username.send_keys(self.user_id)
        password.send_keys(self.user_pass)
        time.sleep(1)
        log_in_button=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div").click()
        time.sleep(5)
        yoksay_button=self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
    def get_profile(self):
        self.following=[]
        self.followers=[]
        profile=self.driver.get(f'https://www.instagram.com/{self.user_id}')
        get_following_button=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(2)
        click_to_box=self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]").click()
        for a in range(250): 
            fBody  = self.driver.find_element_by_xpath("//div[@class='isgrP']")
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            time.sleep(0.2)
        time.sleep(1)
        get_user=self.driver.find_elements_by_tag_name("a")
        for a in get_user:
            self.following.append(a.get_attribute("title"))
        bos=""
        self.filtered_new_following=[]
        for x in self.following:
            if x != bos:
                self.filtered_new_following.append(x)
        print("following list is below!")
        print(self.filtered_new_following)
        close_following=self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        time.sleep(0.2)
        open_followers=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        for a in range(100):        
            fBody  = self.driver.find_element_by_xpath("//div[@class='isgrP']")
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            time.sleep(0.5)
        get_followers=self.driver.find_elements_by_tag_name("a")
        for users in get_followers:
            self.followers.append(users.get_attribute("title"))
        self.filtered_followers=[]
        for non_filtered_users in self.followers:
            if non_filtered_users != bos:
                self.filtered_followers.append(non_filtered_users)
        print("followers list is below")
        print(self.filtered_followers)
        
        self.compare_list=[]
        for following in self.filtered_new_following:
            if following not in self.filtered_followers:
                self.compare_list.append(following)
        
        print("You following but this people not following is below.")
        print(self.compare_list)
        self.non_followers_dict={}
        for non_followers in self.compare_list:
            self.non_followers_dict[non_followers]=(f'https://www.instagram.com/{non_followers}/')    
        print(self.non_followers_dict)
        
        
    def unfollow_method(self):
        while True:
            print("************************************")
            for keys,value in self.non_followers_dict.items():
                print(f' name = {keys} user link = {value}')
            print(f' Total number who doesnt follow you is = {len(self.non_followers_dict)}')
            print("************************************")
            self.input1=input("Do You Want To Unfollow User? [write [y] or [Y]]:")
            if self.input1 == "y" or self.input1 == "Y":
                self.input2=input("Which user do you want to unfollow write down name.:")
                if self.input2 in self.non_followers_dict:
                    self.driver.get(self.non_followers_dict[self.input2])
                    time.sleep(0.5)
                    unf_button=self.driver.find_element_by_xpath("//button[contains(text(),'Takiptesin')]").click() # "//a[@href'accounts/login']" bunun gibi kullanımı var.
                    time.sleep(1)                                                                                   # veya "//input[@name='username']"
                    unf_agreement  =self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
                    time.sleep(0.2)
                    print(f' user {self.input2} is successfully unfollowed!')
                    del self.non_followers_dict[self.input2]
                else:
                    print("There is no name like this.")
            else:
                print("Exiting...")
                break
            
            
user_idx=input("Enter Instagram User ID:")
user_pasx=input("Enter Instagram User Password:")
mecit=InstagramBot(user_idx,user_pasx)
mecit.login()
mecit.get_profile()
mecit.unfollow_method()

