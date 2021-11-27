import csv
from itertools import zip_longest
game_array = []
text_output = ""
with open("games.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        game_array.append(list(row))
console_lists = list(zip(*game_array))
#yeah yeah this is bad, but i want to be able to replace elements in console_lists
for i in range(len(console_lists)):
    given_console = list(console_lists[i])
    while("" in given_console):
        given_console.remove("")
    console_name = given_console[0]
    games = given_console[1:]
    games = sorted(games)
    console_lists[i] = ([console_name] + games)
    text_output+=f"\n<h1>{console_name}</h1>\n<p>\n"
    text_output+="<br>\n".join(games) + "\n</p>"
print(console_lists)
with open('blankpage.html') as template:
    pagetext = template.read()
    header = pagetext.split('<div id="content">')[0] + '<div id="content">\n'
    header = header.replace("Sample Blank Page","My Video Game Collection")
    header = header.replace("Example Page","Game Collection")
    footer = "\n</div>" + pagetext.split("</div>")[-1] + "\n"

with open('games.html','w') as outfile:
    outfile.write(header + text_output + footer)
#output a sorted version of the csv: each console's games alphabetized
with open('games.csv','w') as csv_out:
    outdata = zip_longest(*console_lists,fillvalue='')
    w = csv.writer(csv_out)
    w.writerows(outdata)
