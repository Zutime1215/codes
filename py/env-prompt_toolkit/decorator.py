from prompt_toolkit import prompt

id_name = input("Enter Id: ")
title = input("Enter Name(copy from title tag): ")
vid_link = input("Iframe tag: ")
links = prompt('Paste episodes links:\n ')
openi = input("openings Link: ")
endi = input("endings Link: ")
details2 = input("Enter Details h2: ")
details4 = input("Enter Details h4: ")
details = input("Enter Details: \n")
img = input("Enter Details img tag: ")
pub = int(input("publish year: "))
rela = input("enter id name with "","" format: ")

print(f"""










"{id_name}": {{
		"animetitle": "{title}",
		"animevidlink": `{vid_link}`,
		"animedetailsh2": "{details2}",
		"animedetailsh4": "{details4}",
		"animedetails": `{details}`,
		"animeimg": '{img}',
		"published": {pub},
		"open": `{openi}`,
		"end": `{endi}`,
		"episodelinks": [

			{links}

		],
		"animerelated": [{rela}]
   	}},

""")

