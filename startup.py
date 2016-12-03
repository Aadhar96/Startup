from selenium import webdriver
a=webdriver.Chrome(r'C:/chromedriver.exe')
a.get('http://trak.in/india-startup-funding-investment-2015/')
b=a.find_element_by_tag_name('table')
