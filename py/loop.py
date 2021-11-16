## --- declare variable start

name = 'My Hero Academia'
season_no = 4





episodes = [
	"https://drive.google.com/file/d/1rERUq1cbz82HrPlHWXyildTPd-P6-sxw/preview",
	"https://drive.google.com/file/d/11PGWHwai2RBnnz-q28O6uumYuLMp7H6O/preview",
	"https://drive.google.com/file/d/1M7ULIUffoWlGzWWkNM79Cv1W4QAoJc6j/preview",
	"https://drive.google.com/file/d/1bBOHRgbc6emDYLYaWQSOgS7azNA_N6sq/preview",
	"https://drive.google.com/file/d/1qzBLEsHJfg2WQ2_oHfpvtbJGqCvZPTnC/preview",
	"https://drive.google.com/file/d/1ohtr9CMXQpj2jHsoggsS59YAeZKkEMdy/preview",
	"https://drive.google.com/file/d/1mGopo17fgcdMzcOxx2i1ZVI_3jEBgP5b/preview",
	"https://drive.google.com/file/d/18bRZX_J61q8uzvOMFmYm7pvnY5wwnHcU/preview",
	"https://drive.google.com/file/d/1PQt056ZjEddREk1wODa1N4wgd4uO17x-/preview",
	"https://drive.google.com/file/d/1qonHp0INKNGP-o_TOusLpbKs9mVC68Lj/preview",
	"https://drive.google.com/file/d/136YO1x26PiEvurpre4nbEqs5LMC5dyek/preview",
	"https://drive.google.com/file/d/1x8QcJ46PLwMG29GpCTFgZhINOS757jQS/preview",
	"https://drive.google.com/file/d/1UzniYgjYdkpedio58qWInjToBlqDTT9o/preview",
	"https://drive.google.com/file/d/1n7znm1Z11RElppmS9Fj_NYJ8lTXMjSlA/preview",
	"https://drive.google.com/file/d/1hB8-DBqXZ3nF8bKzNv84CHXnUY4IVifp/preview",
	"https://drive.google.com/file/d/184SfKVe_lOx4ltLfnsFDjBXK_0jPdRsV/preview",
	"https://drive.google.com/file/d/1NeHQ1OgzJIymKupQl4NkUkFFLVLaUIeB/preview",
	"https://drive.google.com/file/d/1bUzgc_0IUDf30XOWkBZe7WXp7GPLcD2W/preview",
	"https://drive.google.com/file/d/1IV7nCe3lHg4PNFOYBQFCVJ-tnROlQeJr/preview",
	"https://drive.google.com/file/d/1RdtLSXndswhuGgYY_Hsb3vU4-ZjB5IzN/preview",
	"https://drive.google.com/file/d/12WXEcnX8pTpdhe7mQ1x1r-aJINaIoPiW/preview",
	"https://drive.google.com/file/d/1CoJJ3He7RFWavAcwYy-yukpj2Y9Giy6f/preview",
	"https://drive.google.com/file/d/13cSNtAH92Cqixx1yI3Mn1OsR3IoFxFJ2/preview",
	"https://drive.google.com/file/d/1q9ti4j1PK2n-Y8jccCPpQSzIOJrltmgZ/preview",
	"https://drive.google.com/file/d/1NmZW0gtRLQ9qn4u01Opk9sdITfkDPMB3/preview"

	
]

## --- declare variable end



# list start

js_list = []

js_list.append('var quoteArry = [') 
for i in range(len(episodes)):
	if i == (len(episodes) - 1):
		js_list.append(f'  "{episodes[i]}"')
	else:
		js_list.append(f'  "{episodes[i]}",')

js_list.append('];') 

# list end



# add next and prev button
js_list.append('''
var current_episode = 0;

var nextbtn = document.querySelector('.nextbtn');
var prevbtn = document.querySelector('.prevbtn');

nextbtn.addEventListener('click', function() { generate_episode(current_episode + 1); });
prevbtn.addEventListener('click', function() { generate_episode(current_episode - 1); });
''')

# add all episode button
for i in range(1, len(episodes) + 1):
	js_list.append(f"""var btn{i} = document.querySelector('.btn{i}');
btn{i}.addEventListener('click', function() {{ generate_episode({i - 1}); }});
""")

# add generate_episode function
js_list.append(f'''
function generate_episode(i) {{
  if (quoteArry[i] === undefined) {{
  	return;
  }}

  current_episode = i;
  document.getElementById('link-1').src = quoteArry[i];
  document.getElementById('link-2').innerHTML = "{name} Season {season_no}  Episode " + (i + 1);
}}
''')

js = '\n'.join(js_list)

with open('player.js', 'w') as f:
	f.write(js)
