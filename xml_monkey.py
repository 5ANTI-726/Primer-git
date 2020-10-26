from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

#SSL certificate ignore
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = "http://py4e-data.dr-chuck.net/comments_836080.xml"

html = urlopen(address,context=ctx).read()
xml  = ET.fromstring(html.decode())
comments = xml.findall('comments/comment')

sum = 0
for comment in comments:
    sum = sum + int(comment.find('count').text)
print(sum)
