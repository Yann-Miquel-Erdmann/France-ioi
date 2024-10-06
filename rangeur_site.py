import requests
import bs4 as bs
import json
import os

# cookies = {
#     "":"eyJpdiI6Ik5uTWxGUytUYlZzM0VrbVJWNFwvUlRBPT0iLCJ2YWx1ZSI6InlmM09GMDZieEZSQ0o3aENobWFlbHFBNFhXTGt1ampKZVlzZ3h1ZEVTVDJzSkppN2grMjRZVE82Zjc0UEVaYm9sZGxMYXhzVGMxNGNGdDA5d2RsUmJnPT0iLCJtYWMiOiI1ZjQ1YzI5NGJkMGYwOTI0ZmI3YTNjZjAyM2VmZWYxYWY2YTJjNTg4YmQzOWE2MGYzNjRiMmM4MWEyZjcyYjk2In0",
#     "":"eyJpdiI6InVWb3JuZFBZdmk3emxGQ0VTRmZOQkE9PSIsInZhbHVlIjoiVk4reUE3ODYrQnhMdkxUZ2xjOEZWM1ozTHF1RXFHVUQya3pPQWRBeCsxVVhjUWhGTFBvWkVxcXNMU1BLcnIrZ2Y3bElOMXI1NWZ3QVJyMWF0SkVqOXc9PSIsIm1hYyI6ImY1ZTAxMmQ0YWYzNjI0NWMzZWZkZTc3Nzc3ODY4MTY4MTQ1OTYyZDVkY2M4NmFlNTA5NGI1ZmFlYzJhOGMyNDAifQ"
# }
# site = requests.get("https://www.france-ioi.org/algo/chapters.php", cookies= {"PHPSESSID": "r463slqlei0t8s2d810d40bti4"})
# with open("site.html", "w") as f:
#     f.write(site.text)
# site = site.text

# with open("site.html") as f:
#     site = f.read()


# soup = bs.BeautifulSoup(site)

# lst = soup.find_all("td")
# chapters = {}
# actual = ""
# for elem in lst:

#     if elem.find("h2"):
#         actual = elem.find("h2")
#         if actual.find("span"):
#             break

#         actual = actual.get_text()
#         chapters.update({actual:[]})
        
#     elif elem.find("a"):
#         val = elem.find("a")
#         text = val.get_text()
#         if " – " in text:
#             text = text.split(" – ")[1]
            
#         chapters[actual].append({"name":text, "link":val['href'] , "exercices":[]})


# with open("structure_site.json", "w", encoding="utf-8") as f:
#     json.dump(chapters, f,ensure_ascii=False)



# for name,chapter in chapters.items():
#     for elem in chapter: 
#         site = requests.get(elem["link"], cookies= {"PHPSESSID": "r463slqlei0t8s2d810d40bti4"})
#         soup = bs.BeautifulSoup(site.text)
#         exercices = soup.find_all("div", class_= "chapter-item-row chapter-task-row")
#         for exercice in exercices:
#             val = exercice.find("a")
#             elem["exercices"].append({"name":val.get_text().split(") ")[1], "link":val["href"]})


with open("structure_site.json", "r", encoding="utf-8") as f:
    chapters = json.load(f)



# here = os.path.dirname(os.path.abspath(__file__))
# for name,chapter in chapters.items():
#     for elem in chapter: 
#         for exercice in elem["exercices"]:
#             if not os.path.isdir(os.path.join(here,f"{name}/{elem['name']}")):
#                 os.makedirs(os.path.join(here,f"{name}/{elem['name']}"))
#             if os.path.exists(os.path.join(here,f"{exercice['name']}.py")):
#                 os.rename(os.path.join(here,f"{exercice['name']}.py"), os.path.join(here,f"{name}/{elem['name']}/{exercice['name']}.py"))






here = os.path.dirname(os.path.abspath(__file__))
for name,chapter in chapters.items():
    for elem in chapter: 
        for exercice in elem["exercices"]:
            if os.path.isfile(os.path.join(here,f"{name}/{elem['name']}/{exercice['name']}.py")):
                with open(os.path.join(here,f"{name}/{elem['name']}/{exercice['name']}.py"), 'r+') as f:
                    content = f.read()
                    f.seek(0, 0)
                    f.write("# Lien vers l'éxercice: "+ exercice["link"]+ '\n\n' + content)



# with open("structure_site.json", "w", encoding="utf-8") as f:
#     json.dump(chapters, f,ensure_ascii=False)




