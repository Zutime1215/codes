from selenium import webdriver

links = []


url = input("anime link paste koro: ")
episode = int(input('episode shongkha ti likho: ')) + 1
outname = input("file er ekta naam de, jei file e link gula save hobe:  ")


with open(outname + '.txt', 'w') as blank:
	blank.write("")

driver = webdriver.Chrome(executable_path='/home/zahid/codes/src/chromedriver')
driver.get(url)


for i in range(1,episode):
	test = driver.find_element_by_xpath(f'''//*[@id="main_bg"]/div[5]/div/div[1]/ul/li[{i}]/a''').get_attribute("href")
	links.append(test)

links.reverse()

for link in links:
	driver.get(link)

	iframe = driver.find_element_by_tag_name("iframe").get_attribute("src")
	name = driver.find_element_by_tag_name("h1").text

	with open(outname + '.txt', 'a') as output:
		output.write(name + '\n')
		output.write(iframe + '\n\n')


driver.close()

