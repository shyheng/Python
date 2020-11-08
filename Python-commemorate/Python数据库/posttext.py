from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request("http://www.thsrc.com.tw/tw/timetable/searchresult")
postData = parse.urlencode([
    ("StartStation", "2f940836-cedc-41ef-8e28-c2336ac8fe68"),
    ("EndStation", "977abb69-413a-4ccf-a109-0272c24fd490"),
    ("DepartueSearchDate", "2020/03/12"),
    ("DepartueSearchTime", "06:00"),
    ("DiscountType", "e1b4c4d9-98d7-4c8c-9834-e1d2528750f1")
])

req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0")
resp = urlopen(req, data=postData.encode("utf-8"))
print(resp.read().decode("utf-8"))
