while True:
	url = input("Paste your url: ")
	url = url.replace("\\","")
	url = url.replace("u0025","%")
	print("\n"url)

	if url == "ex":
		break		