from selenium import webdriver

url = 'https://www.facebook.com/100005421971441/videos/2862459190681999/'

driver = webdriver.Chrome(executable_path='/home/zahid/codes/py/10-min-downloader/chromedriver')
driver.get(url)



driver.find_element_by_id('email').send_keys('agontuk.lmn@gmail.com')
driver.find_element_by_id('pass').send_keys('shantinai007')
driver.find_element_by_id('loginbutton').click();

print(driver.page_source)
# driver.quit()
