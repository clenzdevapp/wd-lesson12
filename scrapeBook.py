# coding=utf8
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

csv_file = open("email_list.csv", "w")

url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()
soup = BeautifulSoup(response)

print soup.html.head.title.string

for link in soup.findAll("a"):
    # ZUGRIFF AUF DEN TEXT DES LINKS
    if link.string == "See full profile":
        # ZUGRIFF AUF EIN ATTRIBUT DES LINKS
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        # AUFRUFEN DER JEWEILIGEN SEITE DES MITGLIEDS VON SMARTNINJA
        persont_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(persont_html)
        # NAME
        name=""
        for singleName in person_soup.findAll("h1"):
            if singleName.string != "Hello, ninja!":
                name=singleName.string
        # EMAIL
        email=""
        email = person_soup.find("span", attrs={"class": "email"}).string
        # CITY
        city=""
        for singleCity in person_soup.findAll("span", attrs={"data-city":True}):
            city=singleCity.string
        # AUSGABE IN CSV-DATEI
        csv_file.write(name+","+email+","+city+"\n")
        print("...")

print("Datei wurde erfolgreich erstellt.")
csv_file.close()