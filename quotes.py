# coding=utf8
from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

#MAIN
def main():
    # INITIALISIERUNG WEBSITE
    url = "http://quotes.yourdictionary.com/theme/marriage/"
    response = urlopen(url).read()
    soup = BeautifulSoup(response)

    print("\nHallo Schatz, hier 5 Zitate zu Ehren unserer Hochzeit. In Liebe Carlos =)\n")

    i=1
    for quote in soup.findAll("p", attrs={"class": "quoteContent"}):
        if i==6:
            break
        else:
            print("Zitat " + str(i) + ": " + quote.string)
            i+=1

if __name__ == '__main__':
    main()