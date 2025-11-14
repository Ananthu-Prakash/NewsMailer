import requests
import send_email as se

api_key= "cf1d2980501d46f692ff68e78abbeb54"
url= "https://newsapi.org/v2/everything?q=tesla&" \
"from=2025-10-14&sortBy=publishedAt&" \
"apiKey=cf1d2980501d46f692ff68e78abbeb54"

request= requests.get(url)
content = request.json()
# print(content["articles"])

body= " "
for article in content["articles"]:
    if article["description"] is not None and article["title"] is not None:
        body= body + article["title"] + "\n" + article["description"] +2*"\n"

# se.send_email(body)
print(body)
