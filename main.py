# - *- coding: utf- 8 - *-

#Production by Famaxth
#Telegram - @por0vos1k


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

path = 'path/to/chromedriver.exe' #you need to change this

def parser():
    driver = webdriver.Chrome(path, chrome_options=options)
    driver.get('https://yandex.ru/pogoda/213')
    weather = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div[5]/a/div[1]/span[2]').text
    city_full_text = driver.find_element_by_xpath('//*[@id="main_title"]').text
    term_value = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div[7]/div[2]/div[2]').text

    city = city_full_text.replace("е", "а")

    print(f'Город: {city.replace("Погода в ", "")}\nТемпература: {weather}°\nВлажность: {term_value}')

parser()
