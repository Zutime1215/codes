from selenium import webdriver

episode = 12 + 1
links = []
url = "https://gogoplay1.com/videos/one-punch-man-dub-episode-12"
driver = webdriver.Chrome(executable_path='../../../src/chromedriver')
driver.get(url)

for i in range(1,episode):
	test = driver.find_element_by_xpath(f'''//*[@id="main_bg"]/div[5]/div/div[1]/ul/li[{i}]/a''').get_attribute("href")
	links.append(test)

print(links)	