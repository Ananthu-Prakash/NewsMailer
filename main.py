import requests

api_key= "cf1d2980501d46f692ff68e78abbeb54"
url= "https://newsapi.org/v2/everything?q=tesla&" \
"from=2025-10-14&sortBy=publishedAt&" \
"apiKey=cf1d2980501d46f692ff68e78abbeb54"

request= requests.get(url)
content = request.json()
# print(content["articles"])

for article in content["articles"]:
    print(article["title"])
