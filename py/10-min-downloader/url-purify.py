while True:
	url = input("Paste your url: ")
	url = url.replace("\\","")
	url = url.replace("u0025","%")
	print(url)

	if url == "exit":
		break		