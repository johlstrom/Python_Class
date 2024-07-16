from bs4 import BeautifulSoup
import requests

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.se/TaylorMade-Noodle-Easy-Distance-dussin/dp/B0CDQH3MYB/ref=sr_1_9?crid=13LR3HMV7Q4QQ&dib=eyJ2IjoiMSJ9.1QWIHEXAxPjHE_8JX71soUeZfaMFZlMqY_aKuvjd3LDX0FtcU7dps_VMO3M9f-JMEJR0eJp0hPzTFz9EkIvgr-E7hxvAN-RvG0R-YqQ-N7vgjg8t-P1K_6wbDMmmMI431F4Zk61jEjXach1oCR2qiVznQcT1Ht4zlUdmJuyGJdYGB180108uZK5gitNIK5r65cOnz2ARdNvOLbl0hbIEc64Dv-7JsKGF7QkKf6PFsFDI3y5u4SpYZXrlSkD3FP__ygSu48uPTFVAklQnTUCRmqUkzt4tWgSCsckGyEzWCfI.C0NlEqTvsnFhBqM4CWe-JmXN9iL8m0uqFShSeXX0R8A&dib_tag=se&keywords=golf+balls&qid=1721111180&sprefix=golf+balls%2Caps%2C86&sr=8-9"

response = requests.get(live_url)

soup = BeautifulSoup(response.content, "html.parser")
#print(soup.prettify())

# Find the HTML element that contains the price
price = soup.find(class_="aok-offscreen").get_text()

# Remove the dollar sign using split

price_without_currency = price.split("$")[1]

# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)