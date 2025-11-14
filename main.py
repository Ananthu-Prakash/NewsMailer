import requests
import send_email as se

topic = "tesla"
api_key= "cf1d2980501d46f692ff68e78abbeb54"
url= "https://newsapi.org/v2/everything?" \
f"q={topic}&" \
"from=2025-10-14&" \
"sortBy=publishedAt&" \
f"apiKey={api_key}&" \
"language=en"

request= requests.get(url)
content = request.json()
# print(content["articles"])

body= " "
for article in content["articles"][:20]:
    if article["description"] is not None and article["title"] is not None:
        body= "Subject: Today's News"+ "\n" + body + article["title"] + "\n" 
        + article["description"] + "\n" + article["url"] +2*"\n"

print(body)
se.send_email(body)

