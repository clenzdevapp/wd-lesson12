# coding=utf8
# IMPORTS
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

# URLS
url = "https://en.wikipedia.org/wiki/Game_of_Thrones"
url_wiki = "https://en.wikipedia.org"


# INITIALISIERUNG 1 WEBSITE
response = urlopen(url).read()
soup = BeautifulSoup(response)


# MAIN
def main():
    viewers_got = 0


    # PARSING 1
    for tag in soup.findAll("th", attrs={"class":None}):
        link = tag.next
        if str(link.string).startswith("Season") and str(link).find("title=")>0:
            url_site = url_wiki + link["href"]


            # INITIALISIERUNG 2 WEBSITE
            response_site = urlopen(url_site).read()
            soup_site = BeautifulSoup(response_site)


            # PARSING 2
            for tag_site in soup_site.findAll("tr", attrs={"class":"vevent"}):
                if tag_site.find("sup"):
                    viewers_got += float(tag_site.find("sup").previous.string)
                    #print viewers_got

    print("\nDie Serie Game of Thrones wird auf dem aktuellen Stand von " + str(viewers_got) + " Millionen Zuschauern geschaut. Wie awesome ist das denn :-O ;-)")


if __name__ == '__main__':
    main()