from requests import get
import telegram_send


URL = "http://beta.mcdgov.info/"
R = get(URL)
if R.status_code != 200:
    telegram_send.send(messages=["FATAL: beta.mcdgov.info is down"])

URL = "https://tracker-gov.makerdao.network/"
R = get(URL)
if R.status_code != 200:
    telegram_send.send(messages=["FATAL: tracker-gov.makerdao.network is down"]) 
