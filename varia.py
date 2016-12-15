import requests


def send_email(me, subject, text):
    config = {
        "to": {
            "test@test.com": {
                "message_id": "",
                "reciver_name": ""
            }},
        "smtp_account": "SMTP_ACCOUNT",
        "subject": subject,
        "text": text,
        "from": me,
    }
    query = requests.post('https://api.emaillabs.net.pl/api/new_sendmail', auth=("APP_KEY", "SECRET_KEY"), data=config,
                          headers={"Content-Type": "application/x-www-form-urlencoded"})

    return query.json()

send_email("piotrb@gmail.com", "test", "testsas")

    #
    #
    # def https_to_http(url):
    #     # changes string to list containing every letter as an element,
    #     # finds s in https (if exist) and deletes it.
    #     # ex. https_to_http("https://dupa.dupa") = "http://dupa.dupa"
    #     url = list(url)
    #     if url[4] == "s":
    #         del url[4]
    #         url = ''.join(url)
    #         return url
    #     else:
    #         url = ''.join(url)
    #         return url
    #
    #
    # def get_all_links(url):
    #     # saves all links from a website to a list and returns it
    #     # content of a site and changes it to a string.
    #     # desired method is some kind of html parsing but whatevs.
    #     response = requests.get(url)
    #     content = str(response.content)
    #     output = []
    #     while content.find('<a href=') != -1:  # checks if there any more links, loops till there are any links
    #         href_pos = content.find('<a href=')  # finds a position of <a href=
    #         starting_pos = content.find('"', href_pos)  # finds a position of a first " after href, eg. start of a link
    #         ending_pos = content.find('"', starting_pos + 1)  # finds next ", which is ending of a link
    #         link = content[starting_pos + 1:ending_pos]  # extracts string between " ", which is a link
    #         output.append(link)  # adds our link to list output
    #         content = content[ending_pos:]  # edits rest of a webpage so it starts just after link we just extracted
    #     if output != '':  # only returns output when there are links, in order not to add empty strings to list
    #         return output
    #     # yeah, it doesn't do anything when there are no links, I want it that way.
    #
    #
    # def crawl(url):
    #     url = https_to_http(url)  # changes any https to http, I guess there is a better way but this works just fine
    #     crawled = [url]  # adds our starting page to crawled list to help avoid looping trought same page.
    #     to_crawl = get_all_links(url)  # gets all urls from starting page and adds it to to_crawl list
    #     count = 0  # a helping counter, whatevs
    #     printcounter = 0  # same
    #     while to_crawl != '':  # when to_crawl list isn't empty (almost never) it loops
    #         for link in to_crawl:  # gets every single url from to_crawl list
    #             if link not in crawled:  # if link from to_crawl wasn't already crawled it:
    #                 del to_crawl[to_crawl.index(link)]  # deletes it from to_crawl list
    #                 if link[0:4] == "http":  # checks if it's a valid http link, not some internal shit
    #                     to_crawl = to_crawl + get_all_links(link)  # if it's it crawls it too and adds its links to to_crawl
    #                 crawled.append(link)  # adds it to crawled list, to avoid loops
    #                 printcounter += 1  # adds 1 to counter
    #                 if printcounter == 10:  # prints counter and crawled links every 10 loops
    #                     count +=10
    #                     print(count)
    #                     print(crawled)
    #                     printcounter = 0
    #             else:
    #                 del to_crawl[to_crawl.index(link)]  # if link already is in crawled it deletes it from to_crawl
    #
    #     return crawled  # when there are no more links to crawl it returns all links (almost never)
    #
    #
    # print(crawl("http://facebook.com"))  # crawls facebook page.

    # import requests


    # header = {'user-agent': '# Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',}
    # url = 'http://www.w3.org/'
    # r = requests.get(url, headers=header)
    # print(r.headers)
    # print(r.request.headers)
