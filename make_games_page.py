import csv
game_array = []
text_output = ""
with open("games.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        game_array.append(list(row))
console_lists = list(zip(*game_array))
for given_console in console_lists:
    given_console = list(given_console)
    while("" in given_console):
        given_console.remove("")
    console_name = given_console[0]
    games = given_console[1:]
    text_output+=f"\n<h1>{console_name}</h1>\n<p>\n"
    text_output+="<br>\n".join(games) + "\n</p>"

with open('blankpage.html') as template:
    pagetext = template.read()
    header = pagetext.split('<div id="content">')[0] + '<div id="content">\n'
    header = header.replace("Sample Blank Page","My Video Game Collection")
    header = header.replace("Example Page","Game Collection")
    footer = "\n</div>" + pagetext.split("</div>")[-1] + "\n"

with open('games.html','w') as outfile:
    outfile.write(header + text_output + footer)
    
