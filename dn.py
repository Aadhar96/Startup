from selenium import webdriver
import warnings
import sys
warnings.filterwarnings("ignore")
y=input()
path=r'C:/chromedriver.exe'
a=webdriver.Chrome(path)
a.get('http://www.sentiment140.com/search?query=%s&hl=en'%y)
x=a.find_element_by_id('username_or_email')
x.send_keys('sachdevaaadhar@gmail.com')
x=a.find_element_by_id('password')
x.send_keys('Ready123')
x=a.find_element_by_id('allow')
x.click()
a.get('http://www.sentiment140.com/search?query=%s&hl=en'%y)
b=a.find_elements_by_css_selector("[class='section positive']")
c=a.find_elements_by_css_selector("[class='section negative']")
d=a.find_elements_by_css_selector("[class='section neutral']")
e=len(b)+len(c)+len(d)
f=len(b)*100//e
g=len(c)*100//e
h=len(d)*100//e
print('Positive Sentiment:',f)
print('Negative Sentiment:',g)
print('Neutral Sentiment:',h)

