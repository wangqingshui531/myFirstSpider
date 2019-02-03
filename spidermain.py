import urllib.parse
import urllib.request

print(str({'word':'hello'}))
#data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding＝'utf8')
print(str(urllib.parse.urlencode({'word':'hello'})))
#response= urllib.request.urlopen('http://httpbin.org/post’, data=data)
#print(response.read())


request = urllib.request.Request('https://www.behance.net')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))