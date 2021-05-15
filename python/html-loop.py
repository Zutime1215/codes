txt = """<li><a href="#" class="btn{value}">{value}</a></li>"""

for i in range(1, 53):

    print(txt.format(value = i))
