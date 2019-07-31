import requests
import scrapy

# Set the target webpage
url = 'http://172.18.58.238/spicyx/'
r = requests.get(url)
print(r.text)

print("Status Code:")
print("\t*", r.status_code)

h = requests.head(url)
print("Header:")
print("**********")

for x in h.headers:
    print("\t", x, ":", h.headers[x])
    print("**********")

#Modify headers user-agent
headers = {
    'User-Agent': 'Mobile'
}

url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)


class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['']

    def parse(self, response):
        cssselector = '//img'
        for x in response.css(cssselector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }