import random
from urllib.request import Request, urlopen

def GeraLink():
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    semlink = False
    while not semlink:
        link = 'https://prnt.sc/'
        for x in range(0, 6):
            link += str((random.choice(letras)))
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read().decode('utf-8')
        webpage = webpage[1848:2048]
        webpage = webpage[:str(webpage).find('.png')+4]
        if (str(webpage).count('//st.prntscr.com/') > 0 or len(webpage) < 12):
            semlink = False
        else:
            return [webpage, link[16:]]
