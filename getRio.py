from ftplib import FTP
import bs4
import calendar
import requests
import time

seconds_in_hour = 60 * 60


def get_list(url, greenwich_time):
    r = requests.get(url)

    soup = bs4.BeautifulSoup(r.text, "html.parser")
    streams = []
    for it in soup.find_all("span"):
        if "data-broadcast-end" in it.attrs and "data-redir" in it.attrs:
            if int(it["data-broadcast-end"]) >= greenwich_time:
                info_dict = {
                    'url': it["data-redir"],
                    'title': it.findChild("span", {"class": "title"}),
                    'time': it.findChild("span", {"class": "time"}),
                    "category": it.findChild("span", {"class": "category"})
                }
                streams.append(info_dict)
    return streams


def get_modified_time(page_index):
    return time.time() + seconds_in_hour * page_index


def get_piwik():
    piwik = """
    <!-- Piwik -->
<script type="text/javascript">
  var _paq = _paq || [];
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//piwik.linuxpl.com/";
    _paq.push(['setTrackerUrl', u+'piwik.php']);
    _paq.push(['setSiteId', 9702]);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
  })();
</script>
<noscript><p><img src="//piwik.linuxpl.com/piwik.php?idsite=9702" style="border:0;" alt="" /></p></noscript>
<!-- End Piwik Code -->
"""
    return piwik

def write_header(f, page_index):
    header = """<!DOCTYPE html>
<html>
<head>
<title>
Transmisje z Rio</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="keywords" content="Rio Rio2016 Igrzyska Olimpijskie Olimpiada ">
<meta name="description" content="Transmisje z Rio">
<style type="text/css">
body {background-color:ffffff;background-repeat:no-repeat;background-position:top left;background-attachment:fixed;}
h1{font-family:Arial;color:000000;}
p {font-family:Arial;font-size:24px;font-style:normal;font-weight:normal;color:000000;}
</style>
""" + get_piwik() + """
</head>
<body>
<h1>Transmisje z Rio godzina
"""
    f.write(header)
    local_time = time.localtime(get_modified_time(page_index))
    f.write(str(local_time.tm_hour) + ":" + str(local_time.tm_min))
    f.write("</h1><p>")


def write_footer(f):
    footer = """</p></body></html>"""
    f.write(footer)

def get_page_filename(page_index):
    filename = "index.html"
    if page_index > 0:
        filename = "rio" + str(page_index) + ".html"
    return filename


def create_page(page_index):
    cur_time = calendar.timegm(time.gmtime(get_modified_time(page_index))) * 1000
    url1 = "http://www.api.v3.tvp.pl/shared/listing.php?portal_name=rio2016.tvp.pl&portal_id=19369963&parent_id=24035157&type=directory_standard&copy=false&direct=true&order=position%2C1&count=-1&epg_start=" \
           + str(cur_time) + "&epg_end=" \
           + str(cur_time) + "&template=epg%2Fdisciplines-listing.html"
    url2 = "http://www.api.v3.tvp.pl/shared/listing.php?portal_name=rio2016.tvp.pl&portal_id=19369963&parent_id=25851771&type=virtual_channel&copy=false&direct=true&order=position%2C1&count=-1&epg_start=" \
           + str(cur_time) + "&epg_end=" \
           + str(cur_time) + "&template=epg%2Fchannels-listing.html"

    streams = get_list(url1, cur_time)
    streams += get_list(url2, cur_time)

    streams = [dict(p) for p in set(tuple(i.items()) for i in streams)]
    streams = sorted(streams, key=lambda k: k['title'].text)
    filename = get_page_filename(page_index)
    with open(filename, 'w') as f:
        write_header(f, page_index)
        for s in streams:
            if s["category"]:
                value = "<a href=""{3}""> {0}: {1} {2}</a><br>\n".format(s["title"].text, s["category"].text,
                                                                         s["time"].text, s["url"])
                f.write(value)
            else:
                value = "<a href=""{2}""> {0} {1}</a><br>\n".format(s["title"].text, s["time"].text, s["url"])
                f.write(value)
        if page_index < 3:
            value = "<a href=""{1}""> {0}</a><br>\n".format(
                "Transmisje kończace się w następnej godzinie", "rio" + str(page_index + 1) + ".html")
            f.write(value)
        write_footer(f)


def send_page(page_index):
    filename = get_page_filename(page_index)
    ftp = FTP('s34.linuxpl.com')
    ftp.login(user='piotrbv', passwd='wyytm2705')
    ftp.cwd('public_html')  # change into "debian" directory
    ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    ftp.quit()


def main():
    while True:
        for i in range(4):
            create_page(i)
        for i in range(4):
            send_page(i)
        ten_minutes = 10*60
        print(time.localtime())
        time.sleep(ten_minutes)

if __name__ == "__main__":
    main()
