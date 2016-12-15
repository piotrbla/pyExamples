import bs4
soup = bs4.BeautifulSoup("<h2><a href=""index.html"">Test</a> </h2>", "html.parser")
for link in soup.find_all("h2"):
    a = link.find("a")
    print(a)
    print(a.get("href"))