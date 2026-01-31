import requests
import pyperclip
ori = requests.get("https://6.ipw.cn/")
ipv6 = ori.text
pyperclip.copy(ipv6)
