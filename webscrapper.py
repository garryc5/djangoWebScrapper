def webscrapper():
    url = "https://www.ideafit.com/fitness-library"
    response = requests.get(url, timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    grabbedfeed = content.find_all("div", attrs={
                                   "class": "box white article teaser large wide nopad has-image clearfix"})
    toReturn = []
    for x in range(5):
        artical = {
            'img': grabbedfeed[x].img.get("src"),
            'link': url + grabbedfeed[x].h3.a.get('href')[16:],
            'headline': grabbedfeed[x].h3.text,
            'discript': grabbedfeed[x].p.text
        }
        toReturn.append(artical)
    return toReturn
