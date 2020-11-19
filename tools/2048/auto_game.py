#!/usr/bin/python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import time

url = 'https://play2048.co/'
browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.get(url)

locator = (By.CLASS_NAME, 'game-message')
WebDriverWait(browser, 5, 0.5).until(EC.presence_of_element_located(locator))
game_message = browser.find_element_by_class_name('game-message')
game_over = game_message.find_element_by_tag_name('p').text
htmlElem = browser.find_element_by_tag_name('html')
directions = [Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT]
score = 0

print('Game start...')

while not game_over:
    random_direction = random.choices(directions)
    htmlElem.send_keys(random_direction)
    game_over = game_message.find_element_by_tag_name('p').text
    time.sleep(.2)
    score = browser.find_element_by_xpath("//div[@class='score-container']").text

print('Game Over...')
print('Your final score was %s.' % score)
browser.quit()

