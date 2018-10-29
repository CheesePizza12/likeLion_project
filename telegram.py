import requests
token = "782567712:AAHp6dCq6sjyg6Ocl4uGYsMsdWvj2TN6XwQ"
method_name= "getUpdates"
url = 'https://api.telegram.org/bot{0}/{1}'.format(token,method_name)
update = requests.get(url).json()
# print(requests.get(url))
# print(url)
print(update['result'][0])


user_id = update["result"][0]['message']['from']['id']
method_name='sendmessage'
msg = '안녕하세요'
msg_url = 'https://api.telegram.org/bot{0}/{1}?chat_id={2}&text={3}'.format(token,method_name,user_id,msg)
print(requests.get(msg_url))



# 코스피 정보를 가져와서 텔레그램 봇으로 보내기
import requests
from bs4 import BeautifulSoup

user_id = update["result"][0]["message"]["from"]["id"]
method_name = "sendmessage"

url_cos = "https://finance.naver.com/sise/"
html_cos = requests.get(url_cos).text
soup_cos = BeautifulSoup(html_cos, 'html.parser')
select = soup_cos.select_one('#KOSPI_now')

msg = select.text
msg_url= 'https://api.telegram.org/bot{0}/{1}?chat_id={2}&text={3}'.format(token, method_name, user_id, msg)
requests.get(msg_url)