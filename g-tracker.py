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


# */5 * * * * /home/ubuntu/airflow-scheduler-monitor/env/bin/python monitor.py
# /home/ubuntu/airflow-scheduler-monitor/env/bin/python /home/ubuntu/trackers-monitor/v-tracker.py
